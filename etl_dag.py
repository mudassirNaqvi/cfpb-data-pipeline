from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from extract import extract_data
from transform import transform_data
from load import load_data
from Database import data_sql

default_args = {
    'owner': 'Mudassir',
    'start_date': datetime(2023, 9, 5),
    'retries': 1,
    # 'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='Assignment',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
) as dag:
    
    task_A = PythonOperator(
        task_id="Extract_data",
        python_callable=extract_data
    )

    task_B = PythonOperator(
        task_id="Dump_MySql",
        python_callable=data_sql
    )

    task_C = PythonOperator(
        task_id="Transform_data",
        python_callable=transform_data
    )

    task_D = PythonOperator(
        task_id="data_load",
        python_callable=load_data
    )

    task_A >> task_B >> task_C >> task_D