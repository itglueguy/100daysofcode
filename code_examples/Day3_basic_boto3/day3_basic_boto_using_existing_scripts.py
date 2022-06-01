# import the module
import boto3

# establisha  session
session = boto3.Session(profile_name='default')

# decompose some existing functions into smaller functions


def generate_credential_report():
    """
    Starts generation of a credentials report about the current account. After
    calling this function to generate the report, call get_credential_report
    to get the latest report. A new report can be generated a minimum of four hours
    after the last one was generated.
    """
    try:
        iam = boto3.resource('iam')
        response = iam.meta.client.generate_credential_report()
        response['State']
    except ClientError:
        logger.exception("Couldn't generate a credentials report for your account.")
        raise
    else:
        return response

def get_credential_report():
    """
    Gets the most recently generated credentials report about the current account.
    :return: The credentials report.
    """
    try:
        iam = boto3.resource('iam')
        response = iam.meta.client.get_credential_report()
        print(response['Content'])
    except ClientError:
        logger.exception("Couldn't get credentials report.")
        raise
    else:
        return response['Content']