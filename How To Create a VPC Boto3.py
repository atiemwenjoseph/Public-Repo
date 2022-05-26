import boto3

ec2 = boto3.client("ec2")
lol = ec2.create_vpc(CidrBlock='10.0.0.0/24')
print(lol)
