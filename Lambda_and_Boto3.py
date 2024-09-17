import boto3
import json

def lambda_handler(event, context):
    ec2_connection = boto3.resource(service_name="ec2", region_name="us-west-2")

    # Stop EC2 instances with tag 'Rajkumar-Auto-Stop'
    stop_filter = {"Name": "tag:Name", "Values": ["Rajkumar-Auto-Stop"]}
    for instance in ec2_connection.instances.filter(Filters=[stop_filter]):
        print(f"Stopping instance: {instance.id}")
        try:
            instance.stop()
        except Exception as e:
            print(f"Error stopping instance {instance.id}: {str(e)}")

    # Start EC2 instances with tag 'Rajkumar-Auto-Start'
    start_filter = {"Name": "tag:Name", "Values": ["Rajkumar-Auto-Start"]}
    for instance in ec2_connection.instances.filter(Filters=[start_filter]):
        print(f"Starting instance: {instance.id}")
        try:
            instance.start()
        except Exception as e:
            print(f"Error starting instance {instance.id}: {str(e)}")

    return {
        'statusCode': 200,
        'body': 'EC2 instances managed based on tags.'
    }
