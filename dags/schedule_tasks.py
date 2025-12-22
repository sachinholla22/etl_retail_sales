from airflow import DAG 
from airflow.operators.python import PythonOperator
from datetime import datetime
from pipelines.extract import upload_to_s3,download_from_s3
import logging
from logs.log_config import setup_config

setup_config()

basic_config={
    
    "start_date":datetime(2025,12,23),
    "retries":1

}


with DAG(
   dag_id="testing_airflow_dag",
   default_args=basic_config,
   schedule_interval="@daily",
   catchup=False

) as dag:
    
    uploadScript=PythonOperator(
        task_id="uploadScript",
        python_callable=upload_to_s3,
        op_args=[]

    )



