# class404/utils.py

def s3_handler(file):
    s3_client = boto3.client(
        's3',
        aws_access_key_id     = s3_config['access_key_id'],
        aws_secret_access_key = s3_config['secret_access_key']
    )
    s3_client.upload_fileobj(
        file, 
        s3_config['bucket_name'],
        file.name,
        ExtraArgs={
            "ContentType": file.content_type
        }
    ) 
    file_url = f'https://{AWS_STORAGE_BUCKET_NAME}.\
        s3.amazonaws.com/{str(file)}'
    return file_url