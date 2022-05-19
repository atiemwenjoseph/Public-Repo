import boto3

# This represents the aws resource "s3"
aws_resource = boto3.resource("s3")

# This represents the name given the bucket
bucket = aws_resource.Bucket("second-bucket-for-bivol")

# This represents the bucket's characteristics
response = bucket.create(
    ACL='private',
    CreateBucketConfiguration={
        'LocationConstraint': 'eu-west-2'
    },

)

print(response)

###########################################################
