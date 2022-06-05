# Import the boto3 module
import boto3
import datetime
# use the client endpoint
client = boto3.client('organizations')

# List all AWS Accounts in the AWS Organization
accounts = client.list_accounts()

print("Account number - Name - Email - Status")

for account in accounts['Accounts']:
    #print(account)
    account_id = account['Id']
    account_name = account['Name']
    account_email = account['Email']
    account_status = account['Status']
    print(account_id + "----------------------------------------------------------")

    # Redefine the client endpoint to connect to the account
    client = boto3.client('sts')

    # python assume role
    assume_role = client.assume_role( RoleArn='arn:aws:iam::'+account_id+':role/AWSControlTowerExecution',RoleSessionName='OrganizationAccountAccessRole')
    #print(assume_role)

    # this seems to access nested key values
    newsession_id = assume_role["Credentials"]["AccessKeyId"]
    newsession_key = assume_role["Credentials"]["SecretAccessKey"]
    newsession_token = assume_role["Credentials"]["SessionToken"]

    # Use the assumed session vars to create a new boto3 client with the assumed role creds
    # Here I create an s3 client using the assumed creds.
    iam = boto3.client(
        'iam',
        region_name='us-east-1',
        aws_access_key_id=newsession_id,
        aws_secret_access_key=newsession_key,
        aws_session_token=newsession_token
    )

    # now i can list all users
    try:
        iam_users = iam.list_users()
    except:
        print("Access issues to " + account_id)
        print("IAM Last used: " + last_used)
        access_keys = iam.list_access_keys(UserName=user['UserName'])
        for item in access_keys['AccessKeyMetadata']:
            #print(item)
            print("    -------------------------------------")
            print("    AccessKeyID: " + item['AccessKeyId'])
            print("    Access Key Status:" + item['Status'])
            print("    Access Key Creation Date: " + item['CreateDate'].strftime("%H:%M:%S"))
    # end code for list all users in 1 account
