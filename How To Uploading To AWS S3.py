import boto3

# How to upload a single file
s3_resource = boto3.client("s3")
# Filename, Bucket and Key are the needed parameter for the file to be uploaded
s3_resource.upload_file(
    Filename="Uploading to AWS S3.py",
    Bucket="first-bucket-for-bivol419",
    Key="Uploading to AWS S3.txt", )
