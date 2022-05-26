import boto3

ec2 = boto3.client("ec2")
delete = ec2.delete_snapshot(SnapshotId='snap-0652b07edeb326a36')

print(delete)

