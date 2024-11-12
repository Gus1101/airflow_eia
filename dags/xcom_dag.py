from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def xcom_write(**kwargs):
    kwargs["ti"].xcom_push(key="task_push_key",value="hello")

def xcom_read(**kwargs):
    value = kwargs["ti"].xcom_pull(key="task_push_key", task_id="task_push")
    print(f"values retrived: {value}")

with DAG(
    dag_id="xcom_dag",
    description="xcom test dag",
    start_date=datetime(2024,11,9),
    schedule_interval="@daily",
    catchup=False,
) as dag:
    
    task_push = PythonOperator(
        task_id = "task_push",
        python_callable=xcom_write,
    )

    task_pull = PythonOperator(
        task_id="task_pull",
        python_callable=xcom_read,
    )

    task_push >> task_pull
    