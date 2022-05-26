import boto3

ec2 = boto3.client("ec2")
ebs = ec2.create_snapshot(Description='snapshot from Boto3',
                          VolumeId='vol-028e4af6a717716c4')
print(ebs)
