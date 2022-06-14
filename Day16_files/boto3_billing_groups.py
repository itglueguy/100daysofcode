import boto3

# Create a new billing conductor resource and specify a region.
# had to update by boto version to use this command
client = boto3.client('billingconductor')


# create a pricing plan
response = client.create_pricing_plan(
    Name='mypricingplan',
    Description='mypricingplan'
)

# list to see existing
pricing_plan_response = client.list_pricing_plans()

pricing_plan_arn = pricing_plan_response['PricingPlans'][0]['Arn']


# This seems to work - i have switched out two number for it to not correspond to my account number
same_account_id = '433788920478'

# So create at least one initial group
response = client.create_billing_group(
    Name='Centralized',
    AccountGrouping={
        'LinkedAccountIds': [
            same_account_id,
        ]
    },
    ComputationPreference={
        'PricingPlanArn': pricing_plan_arn
    },
    PrimaryAccountId=same_account_id,
    Description='my pricing plan'
)

# Add an Account to an existing group
billing_groups = client.list_billing_groups()

# get the arn of the existing billing group
my1_billing_arn = billing_groups['BillingGroups'][0]['Arn']

# associates the an aws account with a billing group
response = client.associate_accounts(
    Arn=my1_billing_arn,
    AccountIds=[
        '342384017843',
    ]
)

