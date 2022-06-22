import boto3

# initiate the object context
client = boto3.client('ec2')

# lists the current snapshots - this is old
client.describe_snapshots(OwnerIds=['self'])

# Created an EC2 Instance to try Snapshot creation and Snapshot deletion


# Get the Vol ID from the instance

instances = client.describe_instances()

# This doesn't work well with more than one instances - but its practice
volume_id = instances['Reservations'][0]['Instances'][0]['BlockDeviceMappings'][0]['Ebs']['VolumeId']

# this will take some time - the response should show the snapshot progress
response = client.create_snapshot(
    Description='My new snapshot',
    VolumeId=volume_id
)

# Lets see what snapshots are available

snapshots = client.describe_snapshots()

#delete it by ID - change it to your relevantid - that was pretty immediate
client.delete_snapshot(SnapshotId='snap-04777f0615eb25130')