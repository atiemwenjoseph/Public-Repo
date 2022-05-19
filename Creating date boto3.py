import boto3

# This represents the aws resource "s3"
s3_resource = boto3.client("s3")
print(s3_resource)

# This represents details about the "s3" namely:
# ResponseMetadata
# Buckets
# Owner
date = s3_resource.list_buckets()
for bivol in date:
    print(bivol)

# This represents the 1st, 2nd, 3rd bucket names respectively
name_b = s3_resource.list_buckets()["Buckets"][0]["Name"]
name_b1 = s3_resource.list_buckets()["Buckets"][1]["Name"]
name_b2 = s3_resource.list_buckets()["Buckets"][2]["Name"]
print(name_b)
print(name_b1)
print(name_b2)

# This represents the creation dates of the
# 1st, 2nd, 3rd bucket names respectively
date_b = date["Buckets"][0]["CreationDate"]
date_b1 = date["Buckets"][1]["CreationDate"]
date_b2 = date["Buckets"][2]["CreationDate"]
print(date_b)
print(date_b1)
print(date_b2)
