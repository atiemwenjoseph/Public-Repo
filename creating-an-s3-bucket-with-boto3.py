import boto3
aws_resource=boto3.resource("s3")
bucket=aws_resource.Bucket("simple-storage-service")
response = bucket.create(
    ACL='public-read',
    CreateBucketConfiguration={
        'LocationConstraint':'eu-west-2'
    },
    
)

print(response)