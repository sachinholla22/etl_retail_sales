import os
import boto3
from botocore.exceptions import ClientError
from logs.log_config import setup_config
import pandas as pd
import logging

setup_config()

def upload_to_s3(bucket_name,object_name,file_name):
    try:
        logging.info("Started uploading file")
        s3_client=boto3.client('s3')
        
        if not object_name:
            object_name=file_name
        try:

            if s3_client.head_object(bucket_name,object_name):
                logging.info("File already exists in the AWS S3")
                return 
        except ClientError as e:
            pass    
        result=s3_client.upload_file(file_name,bucket_name,object_name)
        logging.info(f"The file {file_name} uploaded succeessfully")
         
    except ClientError as e:
        logging.error(f"Error occured during uploads {e}")


def download_from_s3(bucket_name,object_key,local_file_path):
    try:
        logging.info("Downloading from s3")
        s3_client=boto3.client('s3')
        if os.path.exists(local_file_path) and os.getsize(local_file_path)>0:
            logging.info("file already exists in the current location so skipping downloading")
            return 
        res=s3_client.download_file(bucket_name,object_key,local_file_path)
        logging.info(f"File has been donwloaded in the path{local_file_path}")
    except ClientError as e:
        logging.error(f"Error occured while downloading the file , {e}")


def read_csv_file(path):
    logging.info("Reading a csv file and converting it to dataframe")
    return pd.read_csv(path)
