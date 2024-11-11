from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

default_args = {
    'start_date' : datetime(2024,11,9),
    'schedule_interval' : '@daily',
    'catchup' : False,
    'retries' : 1,
    'email' : None
}

with DAG (
    dag_id="default_args",
    description="dag using default_args",
    default_args=default_args
) as dag:
    
    task1 = BashOperator(task_id="tsk1",
                         bash_command="echo 'tsk1'")
    
    task2 = BashOperator(task_id="tsk2",
                         bash_command="echo 'tsk2'")
    
    task1 >> task2