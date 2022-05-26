import boto3
# Indicates the resource used
client = boto3.client("ec2")
# The shows the vpc and its contents
x = client.describe_vpcs()
# How to determine number of VPC in your account
num = x["Vpcs"]
print(len(num))
for name in num:
    print(name['VpcId'])
