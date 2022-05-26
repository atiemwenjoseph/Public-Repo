import boto3

ec2 = boto3.resource("ec2")
make = ec2.create_instances(ImageId='ami-0d729d2846a86a9e7',
                            InstanceType='t2.micro',
                            VPCId="vpc-0a255da1824dda970",
                            MaxCount=4,
                            MinCount=3)
print(make)
