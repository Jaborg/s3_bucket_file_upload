import boto3
import os


client = boto3.client('s3',
                        aws_access_key_id = os.getenv('AWS_ACCESS_KEY'),
                        aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY'))




for file in os.listdir():
    if '.csv' in file:
        upload_file_bucket = 'jacobbucketfirst'
        upload_file_key = 'data/' + str(file)
        client.upload_file(file,upload_file_bucket,upload_file_key)
