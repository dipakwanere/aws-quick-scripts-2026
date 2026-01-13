# Sync local data directory to S3
aws s3 sync data s3://ml-data 

# Copy S3 object locally
aws s3 cp s3://ml-data/data.csv .