import os

from dotenv import load_dotenv
from connection import awsconnectionInfo
from share_file import truncateTable


def deleteObj():
    load_dotenv()
    bucket = os.environ["Bucket"]

    s3 = awsconnectionInfo()
    files = truncateTable()
    for deleting in files:
        s3.delete_object(Bucket=bucket, Key=deleting)
    return "OK"



