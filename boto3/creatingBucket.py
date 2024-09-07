import boto3

# Create an S3 client
client = boto3.client('s3')

# Create a new S3 bucket (use a valid bucket name)
bucket_name = 'firstbucket-by-noor-fatima'  # Valid bucket name example

try:
    response = client.create_bucket(Bucket=bucket_name)
    print(f"Bucket '{bucket_name}' created successfully.")
except client.exceptions.BucketAlreadyExists as e:
    print(f"Bucket already exists: {e}")
except client.exceptions.BucketAlreadyOwnedByYou as e:
    print(f"Bucket already owned by you: {e}")
except Exception as e:
    print(f"Error creating bucket: {e}")


