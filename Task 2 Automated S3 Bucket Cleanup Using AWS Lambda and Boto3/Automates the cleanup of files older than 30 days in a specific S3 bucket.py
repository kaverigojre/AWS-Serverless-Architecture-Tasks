import boto3
from datetime import datetime, timedelta

def lambda_handler(event, context):
    bucket_name = 'kaveris3'
    
    s3_client = boto3.client('s3')

    # List objects in the specified bucket
    response = s3_client.list_objects_v2(Bucket=bucket_name)
    
    # Get the current date
    current_date = datetime.now()

    # Delete objects older than 30 days
    for obj in response.get('Contents', []):
        last_modified = obj['LastModified'].replace(tzinfo=None)
        age = current_date - last_modified

        if age.days > 30:
            s3_client.delete_object(Bucket=bucket_name, Key=obj['Key'])
            print(f"Deleted: {obj['Key']} (Last Modified: {last_modified})")

    print("Cleanup complete.")

