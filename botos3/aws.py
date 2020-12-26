from botocore.exceptions import ClientError
from flask import logging
import random
import string
import datetime
from connection import awsconnectionInfo
import os
from dotenv import load_dotenv
from share_file import insert,select,downloadInsert



class AwsFunctions:
    load_dotenv()

    Bucket = os.environ["Bucket"]

    __s3=awsconnectionInfo()

    __LETTERS = string.ascii_letters
    __NUMBERS = string.digits
    __PUNCTUATION = "!+%&/()=?_#${[]}"
    __printable = f'{__LETTERS}{__LETTERS}{__LETTERS}'
    __printable = list(__printable)

    @staticmethod
    def upload(image,extension,delete_time,obj_size,ip):

        random.shuffle(AwsFunctions.__printable)
        secret_key_first = random.choices(AwsFunctions.__printable, k=20)
        secret_key_first = ''.join(secret_key_first)
        secret_key=secret_key_first+"."+extension
        now = datetime.datetime.now()
        deleted_hour = datetime.datetime.now() + datetime.timedelta(hours=int(delete_time))

        try:
            response = AwsFunctions.__s3.upload_file(image, AwsFunctions.Bucket, secret_key)

            insert(secret_key_first,image,secret_key,now,deleted_hour,obj_size,ip)

            return "Save this key "+ secret_key_first

        except ClientError as e:
            logging.error(e)
            return "Wrong file try again!"

    @staticmethod
    def download(key, ip):
        try:
            file_name,secret_key,size = select(key)
            downloadInsert(ip,size)
            AwsFunctions.__s3.download_file(AwsFunctions.Bucket, file_name, secret_key)
            return "Download Succefull"

        except TypeError as error:
            return "Wrong Key!"







