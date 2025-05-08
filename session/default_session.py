import boto3
from pprint import pprint

# Create an S3 client
s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')

# List all s3 buckets using client object

response = s3_client.list_buckets()
for bucket in response['Buckets']:
    print(bucket['Name'])

# List s3 bucket using resource object
response = s3_resource.buckets.all()
for bucket in response:
    print(bucket.name)
