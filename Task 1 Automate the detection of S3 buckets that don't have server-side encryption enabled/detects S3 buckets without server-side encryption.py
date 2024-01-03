import boto3

def lambda_handler(event, context):
    # Initialize a boto3 S3 client
    s3_client = boto3.client('s3')

    # List all S3 buckets
    response = s3_client.list_buckets()
    buckets = response['Buckets']

    # Detect buckets without server-side encryption
    unencrypted_buckets = []

    for bucket in buckets:
        bucket_name = bucket['Name']
        bucket_encryption = s3_client.get_bucket_encryption(Bucket=bucket_name)

        if not bucket_encryption.get('ServerSideEncryptionConfiguration'):
            unencrypted_buckets.append(bucket_name)

    # Print the names of unencrypted buckets for logging purposes
    if unencrypted_buckets:
        print("Unencrypted S3 Buckets:")
        for unencrypted_bucket in unencrypted_buckets:
            print(unencrypted_bucket)
    else:
        print("All S3 Buckets are encrypted.")

