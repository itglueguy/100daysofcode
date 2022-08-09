# Python 3.8 - extract csv attachment from Mime Email with original attachment name
# 
# Original documentation: https://towardsdatascience.com/extract-email-attachment-using-aws-624614a2429b
# All i did was modify some of the routing and additional parsing to get the attachment name

import json
import boto3
import email
import os
from datetime import datetime
import urllib.parse
import re

def get_timestamp():
    current = datetime.now()
    return(str(current.year) + '-' + str(current.month) + '-' + str(current.day) + '-' + str(current.hour) + '-' + str(current.minute) + '-' + str(current.second))
    
def lambda_handler(event, context):
    # Get current timestamp
    timestamp = get_timestamp()
    
    # Initiate boto3 client
    s3 = boto3.client('s3')
    
    # for manual testing - hash it out so that it can be used for manual testing
    bucket = 'bucket_name_goes_here'
    key = '61arqqvpush8j5e3jjner97b0ni5kl8mltlvjho1'
    
    # Get s3 object contents based on bucket name and object key; in bytes and convert to string
    #data = s3.get_object(Bucket=event['Records'][0]['s3']['bucket']['name'], Key=event['Records'][0]['s3']['object']['key'])
    
    # Allow for manual testing
    data = s3.get_object(Bucket= bucket, Key= key)

    content_type = data['ContentType']
    
    print("Content Type: " + content_type)
    
    contents = data['Body'].read().decode("utf-8")
    print('-----------------')
    find_csv = contents.split(":")
    Extensions = ['.csv','.txt']
    key2 = 'attachment'
    
    for line in find_csv:
        for extension in Extensions:
            if extension in line:
                if key2 in line:
                    print(line)
                    attachment_name = line.split('"')[1]
                    print("the attachment name is: " + attachment_name)
    
    # Given the s3 object content is the ses email, get the message content and attachment using email package
    msg = email.message_from_string(contents)
    print('-----Print the Default Message of the msg object------------')
    print(msg)
    print('-------End----------')
    print('Subject is: ' + msg['subject'])
    print('Address to is: ' + msg['to'])
    subject = msg['subject']
    to = msg['to']
    
    attachment = msg.get_payload()[1]

    fromAddress = msg['from']
    regex = "\\<(.*?)\\>"
    fromAddress = re.findall(regex, fromAddress)[0]

    # Write the attachment to a temp location
    open('/tmp/attach.csv', 'wb').write(attachment.get_payload(decode=True))
    
    # Upload the file at the temp location to destination s3 bucket and append timestamp to the filename
    # Destination S3 bucket is hard coded to 'legacy-applications-email-attachment'. This can be configured as a parameter
    # Extracted attachment is temporarily saved as attach.csv and then uploaded to attach-upload-<timestamp>.csv
    # you can customize the routing based on the from, to, or email address accordingly
    try:
        # Allow for routing engine based on from address and give it a timestamp
        #s3.upload_file('/tmp/attach.csv', 'mbwwitaccountemails', fromAddress + '/attach-upload-' + timestamp + '.csv')
        # get the actual attachment name
        #s3.upload_file('/tmp/attach.csv', 'mbwwitaccountemails', fromAddress + '/' + attachment_name)
        # base the routing on the to address
        s3.upload_file('/tmp/attach.csv', 'bucket_name_goes_here', to + '/' + attachment_name)
        print("Upload Successful")
    except FileNotFoundError:
        print("The file was not found")
    
    # Clean up the file from temp location
    os.remove('/tmp/attach.csv')
    
    return {
        'statusCode': 200,
        'body': json.dumps('SES Email received and processed!')
    }