import boto3
from datetime import datetime, timedelta

def lambda_handler(event, context):
    s3_bucket_name = 'kaveriS3' 
    log_prefix = 'logs/'

    s3 = boto3.client('s3')

    #Accessing the specified S3 bucket and list all log files
    response = s3.list_objects(Bucket=s3_bucket_name, Prefix=log_prefix)

    # Get the current date
    current_date = datetime.now()

    # Checking the age of each log and delete logs older than 90 days
    for log_object in response.get('Contents', []):
        log_last_modified = log_object['LastModified'].replace(tzinfo=None)
        log_age = current_date - log_last_modified

        if log_age > timedelta(days=90):
         
            s3.delete_object(Bucket=s3_bucket_name, Key=log_object['Key']) #deleting log

