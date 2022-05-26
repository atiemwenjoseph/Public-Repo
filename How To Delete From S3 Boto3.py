import boto3
import os

resourcep = boto3.client("s3")
resource_x = resourcep.delete_bucket(Bucket='first-bucket-for-bivol',
                                     Key='python/pic 3.jpeg')
print(resource_x)
