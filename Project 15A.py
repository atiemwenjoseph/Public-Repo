import boto3
# Aim for this task is to stop 3 running instance EC2 Instance
# Ensure that you have running instances


ec2 = boto3.client("ec2")
first = ec2.stop_instances(
    InstanceIds=["i-0a3a58792d5738613"])
second = ec2.stop_instances(
    InstanceIds=["i-02930e68d5a2a4d9e"])
third = ec2.stop_instances(
    InstanceIds=["i-0fb3f990da4628775"])

print(first)
print(second)
print(third)
