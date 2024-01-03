import boto3
import json

def lambda_handler(event, context):
    s3_bucket = 'kaveriS3'
    backup_prefix = 'KaveriS3backup'

    # Initializing a boto3 EC2 and S3 client
    ec2_client = boto3.client('ec2')
    s3_client = boto3.client('s3')

    # Checking if the event is a termination event
    if 'detail' in event and 'eventName' in event['detail'] and event['detail']['eventName'] == 'TerminateInstances':
        # Getting the instance ID from the event
        instance_id = event['detail']['requestParameters']['instancesSet']['items'][0]['instanceId']

        # Describe the EC2 instance to get its details
        instance_description = ec2_client.describe_instances(InstanceIds=[instance_id])
        instance = instance_description['Reservations'][0]['Instances'][0]

        # Create a backup folder with instance ID and timestamp
        backup_folder_name = f"{backup_prefix}_{instance_id}_{context.aws_request_id}"
        backup_folder_path = f"/tmp/{backup_folder_name}"

        # Save necessary files or instance state to the backup folder
        ami_response = ec2_client.create_image(InstanceId=instance_id, Name=f"{backup_folder_name}_ami")
        ami_id = ami_response['ImageId']
        
        # Wait for the AMI creation to complete
        ec2_client.get_waiter('image_available').wait(ImageIds=[ami_id])

        # Copy the AMI to S3
        s3_client.upload_file(f"/tmp/{ami_id}.txt", s3_bucket, f"{backup_folder_name}/{ami_id}.txt")

        print(f"Backup of instance {instance_id} created: {backup_folder_name}")

       


