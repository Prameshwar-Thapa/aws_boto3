# Import the boto3 library
# boto3 is the AWS SDK for Python, allowing you to interact with AWS services like S3, EC2, DynamoDB, etc.
import boto3

# Import pprint for pretty-printing JSON-like data (optional, not used below but helpful in practice)
from pprint import pprint

# ---- Creating Clients and Resources ----

# Create an S3 client object
# Client provides a low-level interface to AWS S3 (direct mapping to AWS service API operations)
s3_client = boto3.client('s3')

# Create an S3 resource object
# Resource provides a high-level, more Pythonic interface to AWS S3 (object-oriented usage)
s3_resource = boto3.resource('s3')

# ---- Listing Buckets Using Client ----

# Use the client object to list all buckets
# This calls the AWS API ListBuckets operation
response = s3_client.list_buckets()

# Loop through each bucket dictionary in the response
for bucket in response['Buckets']:
    # Print the name of each bucket
    print(bucket['Name'])

# ---- Listing Buckets Using Resource ----

# Use the resource object to list all buckets
# 'buckets.all()' returns an iterable of bucket objects
response = s3_resource.buckets.all()

# Loop through each bucket object
for bucket in response:
    # Print the name attribute of each bucket object
    print(bucket.name)


