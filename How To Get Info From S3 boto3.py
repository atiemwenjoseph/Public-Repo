import boto3
import os

client = boto3.client("s3")
objects = client.get_object(Bucket="first-bucket-for-bivol", Key='lol.txt')
data = objects['Body'].read()
print(data)
