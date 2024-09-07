import boto3

# Create an S3 client with a specific region
client = boto3.client('lambda', region_name='us-west-2')

# List Lambda functions
response = client.list_functions()
print(response)
