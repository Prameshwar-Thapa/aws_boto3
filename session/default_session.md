# Import the boto3 library
# boto3 is the AWS SDK for Python, used to interact programmatically with AWS services like S3, EC2, Lambda, etc.
import boto3

# Import pprint module
# pprint stands for 'pretty-print' and formats complex data structures (like dictionaries) in a more readable way.
from pprint import pprint

# --- Create Boto3 Clients and Resources ---

# Create an S3 client
# A client provides a low-level interface directly mapped to AWS service APIs (methods like list_buckets, get_object, etc.)
s3_client = boto3.client('s3')

# Create an S3 resource
# A resource is a higher-level object-oriented abstraction for AWS services (e.g., s3.Bucket, s3.Object)
s3_resource = boto3.resource('s3')

# --- List All S3 Buckets Using Client ---

# Use the client object to call 'list_buckets'
# This makes an HTTP request to AWS S3 and retrieves a list of all buckets owned by the account
response = s3_client.list_buckets()

# Loop over each bucket returned in the response
# The response['Buckets'] is a list of dictionaries, each representing one bucket
for bucket in response['Buckets']:
    # Each bucket dictionary contains 'Name' and 'CreationDate'
    # Here, we are printing only the 'Name' key of each bucket
    print(bucket['Name'])

# --- List All S3 Buckets Using Resource ---

# Use the resource object to access all S3 buckets
# s3_resource.buckets.all() returns a collection of Bucket resource objects
response = s3_resource.buckets.all()

# Loop through each Bucket object
for bucket in response:
    # Each 'bucket' is a Bucket resource object, and 'bucket.name' is an attribute that holds the bucket name
    print(bucket.name)
