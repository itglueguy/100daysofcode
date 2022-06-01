import boto3

session = boto3.Session(profile_name='default')

s3 = session.client('s3')

buckets = s3.list_buckets()

for bucket in buckets['Buckets']:
    name = bucket['Name']
    creationdate = bucket['CreationDate'].strftime("%H:%M:%S")
    print(name + "-" + creationdate)
