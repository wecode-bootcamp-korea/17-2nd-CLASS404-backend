import uuid 

import boto3

from my_settings     import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUKET_NAME


class S3FileManager:
    def __init__(self):
        self.s3 = boto3.client(
                's3',
                aws_accesskey_id = AWS_ACCESS_KEY_ID,
                AWS_SECRET_ACCESS_KEY = AWS_SECRET_ACCESS_KEY
                )


    def file_uploader(self, file, file_name):
        self.s3.upload_filobj
