from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG('proximus_pipeline', start_date=datetime(2025,1,1), schedule_interval='@daily') as dag:
    ingest = BashOperator(task_id='ingest_batch', bash_command='echo ingest')
    dataflow = BashOperator(task_id='run_dataflow', bash_command='echo dataflow')
    bq = BashOperator(task_id='load_bq', bash_command='echo bq')
    ingest >> dataflow >> bq
