import boto3
import json
from botocore.exceptions import ClientError

# Initialize clients
s3_client = boto3.client('s3')
sns_client = boto3.client('sns')
sns_topic_arn = 'arn:aws:sns:us-west-2:975050024946:rajkumar-S3PublicAccessAlert'

def check_bucket_acl(bucket_name):
    try:
        # Get the bucket's ACL
        acl = s3_client.get_bucket_acl(Bucket=bucket_name)
        for grant in acl['Grants']:
            grantee = grant['Grantee']
            permission = grant['Permission']
            
            # Check if the grantee is the 'AllUsers' group (public)
            if grantee.get('URI') == 'http://acs.amazonaws.com/groups/global/AllUsers':
                if permission in ['READ', 'WRITE']:
                    return True
        return False
    except Exception as e:
        print(f"Error checking ACL for {bucket_name}: {e}")
        return False

def check_bucket_policy(bucket_name):
    try:
        # Get the bucket's policy
        policy = s3_client.get_bucket_policy(Bucket=bucket_name)
        policy_statements = json.loads(policy['Policy'])['Statement']
        
        for statement in policy_statements:
            if statement['Effect'] == 'Allow':
                principal = statement['Principal']
                action = statement['Action']
                
                if principal == "*" and ('s3:GetObject' in action or 's3:PutObject' in action):
                    return True
        return False
    except ClientError as e:
        # Handle the case when there is no bucket policy
        if e.response['Error']['Code'] == 'NoSuchBucketPolicy':
            return False
        else:
            print(f"Error checking policy for {bucket_name}: {e}")
            return False

def audit_buckets():
    try:
        # List all S3 buckets
        buckets = s3_client.list_buckets()
        public_buckets = []

        for bucket in buckets['Buckets']:
            bucket_name = bucket['Name']
            
            # Check if the bucket has public access
            if check_bucket_acl(bucket_name) or check_bucket_policy(bucket_name):
                public_buckets.append(bucket_name)

        # If any public buckets are found, send an SNS notification
        if public_buckets:
            message = f"The following S3 buckets have public access: {', '.join(public_buckets)}"
            sns_client.publish(
                TopicArn=sns_topic_arn,
                Message=message,
                Subject='Public S3 Bucket Alert'
            )
        else:
            print("No public buckets found.")
            
    except Exception as e:
        print(f"Error auditing S3 buckets: {e}")

def lambda_handler(event, context):
    audit_buckets()
