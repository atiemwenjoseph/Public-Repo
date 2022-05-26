import boto3
import os

client = boto3.client('s3')  # Resources

for file in os.listdir():  # Files in current working directory
    if '.jpeg' in file:
        upload_file_bucket = 'first-bucket-for-bivol'  # name of bucket
        upload_file_key = 'python/' + str(file)
        client.upload_file(file, upload_file_bucket, upload_file_key)
