import boto3

# Create an S3 client
client = boto3.client('s3')

response = client.list_buckets()
# print(response)
# print(response['Buckets'])
print(response[{'Buckets': 'Name'}])