import boto3

# Create S3 client
s3 = boto3.client('s3')

# List S3 buckets  
response = s3.list_buckets()
print(response['Buckets'])