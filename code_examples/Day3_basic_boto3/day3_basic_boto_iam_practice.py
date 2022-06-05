import boto3

# initiate the client
session = boto3.Session(profile_name='default')

# filter to the iam client
iam = session.client('iam')

# get the iam users
iam_users = iam.list_users()

iam_user_list = ['1']

for user in iam_users['Users']:
    print("############################################")
    print("Username: " + user['UserName'])
    print("UserID: " + user['UserId'])
    print("ARN: " + user['Arn'])
    last_used = user['CreateDate'].strftime("%m/%d/%Y")
    print("IAM Creation Date: " + last_used)
    access_keys = iam.list_access_keys(UserName=user['UserName'])
    for item in access_keys['AccessKeyMetadata']:
        #print(item)
        print("    -------------------------------------")
        print("    AccessKeyID: " + item['AccessKeyId'])
        print("    Access Key Status:" + item['Status'])
        print("    Access Key Creation Date: " + item['CreateDate'].strftime("%m/%d/%Y"))
    mfa_devices = iam.list_mfa_devices(UserName=user['UserName'])
    for item in mfa_devices['MFADevices']:
        print("    -------------------------------------")
        print("    MFA Device Serial: " + item['SerialNumber'])
        print("    MFA Device Status: " + item['Status'])
        print("    MFA Device Create Date: " + item['EnableDate'].strftime("%m/%d/%Y"))
    # This method converts a dict to json and bypasses the date not serializable issue
        json_string = json.dumps(user, indent=4, sort_keys=True, default=str)
