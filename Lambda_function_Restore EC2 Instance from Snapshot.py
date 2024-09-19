import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    # Step 1: Define the instance ID
    instance_id = 'i-016cb1676ee69a066'  # Replace with the source instance ID
    
    # Step 2: Fetch the volume ID and its attached availability zone
    volumes = ec2.describe_volumes(
        Filters=[
            {'Name': 'attachment.instance-id', 'Values': [instance_id]}
        ]
    )
    
    if not volumes['Volumes']:
        raise Exception(f"No volumes found for instance {instance_id}")
    
    volume_id = volumes['Volumes'][0]['VolumeId']
    availability_zone = volumes['Volumes'][0]['AvailabilityZone']  # Fetch the AZ dynamically
    
    # Step 3: Fetch the most recent snapshot of the given volume
    snapshots = ec2.describe_snapshots(
        Filters=[
            {'Name': 'volume-id', 'Values': [volume_id]},
        ],
        OwnerIds=['self']
    )
    
    if not snapshots['Snapshots']:
        raise Exception(f"No snapshots found for volume {volume_id}")
        
    # Get the most recent snapshot
    latest_snapshot = max(snapshots['Snapshots'], key=lambda s: s['StartTime'])
    snapshot_id = latest_snapshot['SnapshotId']
    
    # Step 4: Launch a new EC2 instance using the snapshot
    instance = ec2.run_instances(
        ImageId='ami-084f1c3f244e0f2ce',  # Replace with a valid AMI ID
        InstanceType='t4g.nano',  # Adjust the instance type if necessary
        KeyName='Rajkumar_Vired_Ubantu',  # Replace with your EC2 key pair
        MinCount=1,
        MaxCount=1,
        BlockDeviceMappings=[
            {
                'DeviceName': '/dev/sda1',  # Adjust to match your root device name
                'Ebs': {
                    'SnapshotId': snapshot_id,  # Use SnapshotId, not VolumeId
                    'DeleteOnTermination': True,
                    'VolumeType': 'gp2'  # Optional, can specify the volume type
                }
            }
        ],
        Placement={
            'AvailabilityZone': availability_zone  # Ensure the instance is launched in the correct AZ
        }
    )
    
    # Step 5: Get the new instance ID
    new_instance_id = instance['Instances'][0]['InstanceId']
    
    return {
        'statusCode': 200,
        'body': f'New EC2 instance created with instance ID: {new_instance_id}'
    }
