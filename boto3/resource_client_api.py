

# Why Use Session?


# Flexibility: You can configure multiple clients or resources using a single session, which allows for consistency in credentials and regions.

# Profile Management: When dealing with multiple AWS accounts, you can switch between profiles without manually changing credentials.

# Customization: You can specify specific parameters (like region, credentials) during session creation to customize how the session behaves.

# In simple terms, a Boto3 session is like a "connection setup" to AWS. It keeps track of your:

# Credentials (your AWS access key and secret key to prove who you are),
# Region (like which AWS data center you want to use, e.g., us-east-1),
# Profile (if you have multiple AWS accounts, you can switch between them).
# You create a session once and use it to connect to different AWS services (like S3, EC2) without setting up everything again.

# The session object is the starting point for creating clients and resources. You can create a session using the default profile or specify a profile name. You can also specify the region when creating a session.


import boto3

def list_buckets_resource():
    # Create a session using the default profile
    session = boto3.Session()
    
    # Create an S3 resource
    s3_resource = session.resource('s3')
    
    # List all buckets
    print("Buckets using Resource API:")
    for bucket in s3_resource.buckets.all():
        print(bucket.name)

def list_buckets_client():
    # Create a session using the default profile
    session = boto3.Session()
    
    # Create an S3 client
    s3_client = session.client('s3')
    
    # List all buckets
    print("Buckets using Client API:")
    response = s3_client.list_buckets()
    for bucket in response['Buckets']:
        print(bucket['Name'])

if __name__ == "__main__":
    list_buckets_resource()
    list_buckets_client()


# response = s3_client.list_buckets() returns a dictionary that contains the list of S3 buckets under the key 'Buckets'.
# You need to access response['Buckets'], which contains a list of dictionaries, each representing a bucket.






# Without using Session explicitly
def list_buckets_resource():
    s3_resource = boto3.resource('s3')
    print("Buckets using Resource API:")
    for bucket in s3_resource.buckets.all():
        print(bucket.name)

def list_buckets_client():
    s3_client = boto3.client('s3')
    print("Buckets using Client API:")
    response = s3_client.list_buckets()
    for bucket in response['Buckets']:
        print(bucket['Name'])

if __name__ == "__main__":
    list_buckets_resource()
    list_buckets_client()
