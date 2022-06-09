# import the boto3 library
import boto3
import random

# use the aws credential file and set the region
session = boto3.Session(profile_name='default', region_name='us-east-1')

# use the client s3 endpoint
s3 = session.client('s3')

# accept input - doesn't work that well interactivity
bucket_name = 'mybucketname'

# get a random value
random_value = random.randint(1, 99999999)

# make sure the name is tryly random and not likely to be created
bucket_with_random = bucket_name + str(random_value)


print(bucket_with_random)

# create the bucket - should use a while function to make it resilient
try:
    s3.create_bucket(Bucket=bucket_with_random)
except:
    print('Bucket already exists')

# see if the bucket exist
buckets = s3.list_buckets()

bucket_found = 0

# this is the method to find the bucket using a for loop
for bucket in buckets['Buckets']:
    if bucket['Name'] == bucket_with_random:
        bucket_found = 1
        print('Bucket found - ' + bucket_with_random)
        break
print(bucket_found)


# try deleting the bucket
s3.delete_bucket(Bucket=bucket_with_random)
print('Bucket deleted - ' + bucket_with_random)
