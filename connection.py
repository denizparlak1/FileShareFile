import os
import boto3




def awsconnectionInfo():
    access_key = os.environ["AWS_ACCESS_KEY_ID"]
    secret_key = os.environ["AWS_SECRET_ACCESS_KEY"]

    s3 = boto3.client('s3', region_name="us-east-2",
                      aws_access_key_id=access_key,
                      aws_secret_access_key=secret_key)
    return s3
