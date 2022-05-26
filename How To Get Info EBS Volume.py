import boto3

ec2 = boto3.client("ec2")
details = ec2.describe_snapshots(SnapshotIds=['snap-0bd0fd2bb9d1af789'])

print(details)
