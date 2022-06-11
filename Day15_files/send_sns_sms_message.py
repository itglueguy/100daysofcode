import boto3

# Create a new SNS resource and specify a region.
client = boto3.client('sns',region_name='us-east-1')

# Find the ARN containing MyCell in it
for topic in client.list_topics()['Topics']:
    if 'Mycell' in topic['TopicArn']:
        my_topic_arn = topic['TopicArn']
        print(my_topic_arn)



subscriptions = client.list_subscriptions_by_topic(
    TopicArn=my_topic_arn
)

#
my_subscription = subscriptions['Subscriptions']

# the Publish method seems to send a topic to my intended subscription

sns = boto3.client('sns')
number = my_subscription[0]['Endpoint']
sns.publish(
    PhoneNumber = number,
    Message='example text message',
    Subject='my test message'
)


# lets define a function - messages send, but i don't seem to receive the messages
# for some reason
def send_sms(number, message):
    sns = boto3.client('sns')
    sns.publish(PhoneNumber = number, Message=message)

send_sms(number, 'my example text message')


