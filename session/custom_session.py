import boto3
from pprint import pprint

aws_management_console = boto3.session.Session(profile_name = "prameshwar")
aws_ec2_client = aws_management_console.client(service_name = "ec2", region_name = "us-east-1")
aws_ec2_resource = aws_management_console.resource(service_name = "ec2", region_name = "us-east-1")

# List all the ec2

response = aws_ec2_client.describe_instances()
for instance in response['Reservations']:
    for instance_id in instance['Instances']:
        pprint(instance_id['InstanceId'])

# Listing EC2 instances using Resource
response = aws_ec2_resource.instances.all()
for instance in response:
    pprint(instance.id)