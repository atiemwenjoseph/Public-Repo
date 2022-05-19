import boto3

# This represents the aws resource "s3"
resource = boto3.resource("s3")
print(resource)

# This represents all the bucket names as a list
print(list(resource.buckets.all()))

bucket_list = list(resource.buckets.all())
# The number of buckets
print(len(bucket_list))

for bucket in resource.buckets.all():
    print(bucket.name)

    ##########################################

