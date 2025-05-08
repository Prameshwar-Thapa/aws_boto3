✨ What is a Session in Boto3?

In Boto3, a Session is an object that stores configuration details about:

    AWS Credentials (Access Key, Secret Key, Session Token)

    AWS Region

    AWS Profile (if multiple accounts)

    Advanced configurations (like retries, timeouts, etc.)

Every time you make a connection to AWS services via Boto3 (like client('s3') or resource('ec2')), there is a Session involved in the background.

    If you don't create it manually, Boto3 automatically creates a "default session" for you.

    If you want more control, you can create a custom session.

⚡ Why are Sessions Important?

    Credential Management:
    Use different AWS credentials easily (e.g., different AWS accounts).

    Region Management:
    Set different regions for different operations (e.g., us-east-1, ap-southeast-2).

    Multi-Account Automation:
    Operate with multiple AWS profiles/accounts in the same script safely.

    Configuration Control:
    Fine-tune retries, timeouts, and other behavior for API calls.

🛠️ Default Session vs Custom Session
Feature	Default Session	Custom Session
Creation	Implicit (automatic)	Explicit (you create it manually)
Credentials	Pulled automatically (env variables, config files)	You define access keys or profile manually
Region	Pulled automatically from environment or config file	You define manually
Use Case	Simple, quick scripts using 1 AWS account/region	Complex automation with multiple accounts/regions
Control Level	Minimal	Full control over everything
Example	boto3.client('s3')	session.client('s3') after creating Session()
🔥 Default Session (Automatic)

When you directly use boto3.client() or boto3.resource() without creating a session, Boto3 creates a default session internally.

✅ Good for quick scripts where you:

    Have one AWS account,

    Are okay with default credentials and default region.

Example: Default Session

import boto3

# Boto3 automatically creates a default session
s3 = boto3.client('s3')

# Now use it
buckets = s3.list_buckets()
for bucket in buckets['Buckets']:
    print(bucket['Name'])

➔ Here, no session is manually created!
➔ Credentials/region are automatically picked from environment or ~/.aws/credentials.
🔥 Custom Session (Manual)

When you need full control (e.g., switching AWS profiles, using different regions, or temporary credentials), create a session manually.

✅ Best for production apps, multi-account automation, or serverless programming.
Example: Custom Session

import boto3

# Create a custom session
session = boto3.Session(
    aws_access_key_id='YOUR_ACCESS_KEY_ID',
    aws_secret_access_key='YOUR_SECRET_ACCESS_KEY',
    region_name='ap-southeast-2'   # Sydney region
)

# Now create clients/resources using this session
s3 = session.client('s3')
buckets = s3.list_buckets()
for bucket in buckets['Buckets']:
    print(bucket['Name'])

➔ You explicitly define everything: credentials, region.
🎯 Working with AWS Named Profiles

If you have configured multiple profiles in ~/.aws/credentials, you can select the profile via Session:

aws configure --profile dev-account
aws configure --profile prod-account

Now, in Python:

import boto3

# Use "dev-account" profile
session_dev = boto3.Session(profile_name='dev-account')
ec2_dev = session_dev.client('ec2')

# Use "prod-account" profile
session_prod = boto3.Session(profile_name='prod-account')
ec2_prod = session_prod.client('ec2')

➔ This lets you access multiple accounts simultaneously 🔥.
