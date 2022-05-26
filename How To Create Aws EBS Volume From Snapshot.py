import boto3

ec2 = boto3.client("ec2")
ebs = ec2.create_volume(AvailabilityZone='eu-west-2',
                        Encrypted=True,
                        Size=8,
                        SnapshotId='snap-0652b07edeb326a36',
                        VolumeType='gp2')
print(ebs)