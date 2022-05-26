import boto3
import constant
# Indicates the resource and region used
ec2 = boto3.resource("ec2")
# These are parameters used in making the Instance
make = ec2.create_instances(InstanceType='t2.micro',
                            MaxCount=1,
                            MinCount=1,
                            ImageId='ami-0d729d2846a86a9e7')
print(make)
