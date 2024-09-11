import boto3

# Initialize EC2 client
ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    # List to hold instances to start and stop
    instances_to_start = []
    instances_to_stop = []

    try:
        # Describe instances with the tag Auto-Start=True
        start_response = ec2.describe_instances(
            Filters=[
                {'Name': 'tag:Rajkumar-Auto-Start', 'Values': ['True']}
            ]
        )

        # Collect instance IDs for instances that should be started
        for reservation in start_response['Reservations']:
            for instance in reservation['Instances']:
                if instance['State']['Name'] == 'stopped':
                    instances_to_start.append(instance['InstanceId'])

        # Describe instances with the tag Auto-Stop=True
        stop_response = ec2.describe_instances(
            Filters=[
                {'Name': 'tag:Rajkumar-Auto-Stop', 'Values': ['True']}
            ]
        )

        # Collect instance IDs for instances that should be stopped
        for reservation in stop_response['Reservations']:
            for instance in reservation['Instances']:
                if instance['State']['Name'] == 'running':
                    instances_to_stop.append(instance['InstanceId'])

        # Start instances
        if instances_to_start:
            ec2.start_instances(InstanceIds=instances_to_start)
            print(f"Started instances: {instances_to_start}")

        # Stop instances
        if instances_to_stop:
            ec2.stop_instances(InstanceIds=instances_to_stop)
            print(f"Stopped instances: {instances_to_stop}")

    except Exception as e:
        print(f"Error managing EC2 instances: {str(e)}")

    return {
        'statusCode': 200,
        'body': 'Lambda function executed successfully'
    }
