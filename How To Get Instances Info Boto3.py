import boto3

ec2 = boto3.client("ec2")  # Resources
info = ec2.describe_instances()
data = info["Reservations"][0]
instance_data = data["Instances"]
for details in range(len(instance_data)):
    print(f"This is your instance ID {instance_data[details]['InstanceId']}")
