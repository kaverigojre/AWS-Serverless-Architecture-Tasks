# AWS-Serverless-Architecture-Tasks
AWS Serverless Architecture Tasks 

Task 1 : Automate the detection of S3 buckets that don't have server-side encryption enabled.

Instructions:

1. S3 Setup:

   - Navigate to the S3 dashboard and create a few buckets. Ensure that a couple of them don't have server-side encryption enabled.

2. Lambda IAM Role:

   - In the IAM dashboard, create a new role for Lambda.

   - Attach the `AmazonS3ReadOnlyAccess` policy to this role.

3. Lambda Function:

   - Navigate to the Lambda dashboard and create a new function.

   - Choose Python 3.x as the runtime.

   - Assign the IAM role created in the previous step.

   - Write the Boto3 Python script to:

     1. Initialize a boto3 S3 client.
     2. List all S3 buckets.
     3. Detect buckets without server-side encryption.
     4. Print the names of unencrypted buckets for logging purposes.

4. Manual Invocation:

   - After saving your function, manually trigger it.

   - Review the Lambda logs to identify the buckets without server-side encryption.


Task 2: Automated S3 Bucket Cleanup Using AWS Lambda and Boto3

Objective: To gain experience with AWS Lambda and Boto3 by creating a Lambda function that will automatically clean up old files in an S3 bucket.

Task: Automate the deletion of files older than 30 days in a specific S3 bucket.

Instructions:

1. S3 Setup:

   - Navigate to the S3 dashboard and create a new bucket.

   - Upload multiple files to this bucket, ensuring that some files are older than 30 days (you may need to adjust your system's date temporarily for this or use old files).

2. Lambda IAM Role:

   - In the IAM dashboard, create a new role for Lambda.

   - Attach the `AmazonS3FullAccess` policy to this role. (Note: For enhanced security in real-world scenarios, use more restrictive permissions.)

3. Lambda Function:

   - Navigate to the Lambda dashboard and create a new function.

   - Choose Python 3.x as the runtime.

   - Assign the IAM role created in the previous step.

   - Write the Boto3 Python script to:

     1. Initialize a boto3 S3 client.
     2. List objects in the specified bucket.
     3. Delete objects older than 30 days.
     4. Print the names of deleted objects for logging purposes.

4. Manual Invocation:

   - After saving your function, manually trigger it.

   - Go to the S3 dashboard and confirm that only files newer than 30 days remain.


Task 3:Autosave EC2 Instance State Before Shutdown

Objective: Before an EC2 instance is shut down, automatically save its current state to an S3 bucket.

Instructions:

1. Create a Lambda function.

2. Using Boto3, the function should:

   1. Detect when an EC2 instance is about to be terminated.
   2. Save the current state or necessary files from the EC2 instance to an S3 bucket.

3. Use CloudWatch Events to trigger this Lambda function whenever an EC2 termination command is detected.


Task 4: Implement a Log Cleaner for S3

Objective: Create a Lambda function that automatically deletes logs in a specified S3 bucket that are older than 90 days.

Instructions:

1. Create a new Lambda function.

2. Using Boto3, configure the function to:

   1. Access the specified S3 bucket.
   2. List all the log files.
   3. Check the age of each log.
   4. Delete logs older than 90 days.

3. Schedule this function to run weekly using AWS EventBridge.