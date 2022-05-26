import boto3
# Indicates the resource used
vpc = boto3.client("ec2")
# This determines the VPC to be deleted
vpc_removal = vpc.delete_vpc("vpc-vpc-077acf21d92bfbda4")
print(vpc_removal)
