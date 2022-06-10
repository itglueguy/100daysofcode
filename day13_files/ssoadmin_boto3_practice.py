# import the boto3 library
import boto3
import json

# use the aws credential file and set the region
session = boto3.Session(profile_name='default', region_name='us-east-1')

# use the client s3 endpoint
ssoadmin = session.client('sso-admin')

# get the instance arn
instances = ssoadmin.list_instances()

# isolate the instance arn
instance_arn = instances['Instances'][0]['InstanceArn']

# need more permission sets
permission_sets = ssoadmin.list_permission_sets(
    InstanceArn=instance_arn
)

# get the listing task out of the way
for permission in permission_sets['PermissionSets']:
    print('----------------------------------------------')
    print(permission)
    
    response = ssoadmin.get_inline_policy_for_permission_set(
    InstanceArn=instance_arn,
    PermissionSetArn=permission
    )
    
    # print the inline policy if it exists
    try:
        print(response['InlinePolicy'])
    except:
        print(response)

# that took way too long
response = ssoadmin.create_permission_set(
    Name='mynewpermissionset',
    Description='my new permission set',
    InstanceArn=instance_arn,
    RelayState='https://www.google.com'
    )

permissionset_arn = response['PermissionSet']['PermissionSetArn']


# Attach the poweruser permission to the permission set
response = ssoadmin.attach_managed_policy_to_permission_set(
    InstanceArn=instance_arn,
    PermissionSetArn=permissionset_arn,
    ManagedPolicyArn='arn:aws:iam::aws:policy/PowerUserAccess'
)

print(response)

# dict
s3_dict = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:*",
                "s3-object-lambda:*"
            ],
            "Resource": "*"
        }
    ]
}

# dict to json string
json_string = json.dumps(s3_dict)

# put an inline policy - in this case the full s3 policy
response = ssoadmin.put_inline_policy_to_permission_set(
    InstanceArn=instance_arn,
    PermissionSetArn=permissionset_arn,
    InlinePolicy=json_string
)