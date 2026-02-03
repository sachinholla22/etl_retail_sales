from airflow import DAG 
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from pipelines.extract import upload_to_s3,download_from_s3
import logging
import os
from common.log_config import setup_config


setup_config()
local_csv_path=r"C:\Users\sachi\Downloads\hospital_data"
bucket="amazon-aws-200122"
object_name="sales/"
file_name="retail_sales.csv"
directory=os.path.abspath("../datas/raw/")
local_destination=os.path.join(directory,"local_copy.csv")

basic_config={
    
    "start_date": datetime.now() - timedelta(days=1),
    "retries":1

}


with DAG(
   dag_id="testing_airflow_dag",
   default_args=basic_config,
  
   catchup=False

) as dag:
    
    uploadScript=PythonOperator(
        task_id="uploadScript",
        python_callable=upload_to_s3,
        op_args=[bucket,object_name,file_name],

    )

    downloadScript=PythonOperator(
        task_id="downloadScript",
        python_callable=download_from_s3,
        op_args=[bucket,object_name,local_destination],

    )

    uploadScript >> downloadScript



