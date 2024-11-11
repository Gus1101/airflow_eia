from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.task_group import TaskGroup
from datetime import datetime

with DAG(
    dag_id="task_group_dag",
    description="my task group dag",
    start_date=datetime(2024, 11, 9),
    schedule="@daily",
    catchup=False
) as dag:
    
    start_task = BashOperator(
        task_id="start_task",
        bash_command="echo 'start_task'"
    )

    with TaskGroup("ProcessingTask") as processing_tasks:

        processing_task_1 = BashOperator(
            task_id="processing_task_1",
            bash_command="echo 'processing task 1'"
        )

        processing_task_2 = BashOperator(
            task_id="processing_task_2",
            bash_command="echo 'processing task 2'"
        )

        processing_task_3 = BashOperator(
            task_id="processing_task_3",
            bash_command="echo 'processing task 3'"
        )

        [processing_task_1, processing_task_2] >> processing_task_3

    final_task = BashOperator(
        task_id="final_task",
        bash_command="echo 'final_task'"
    )

    start_task >> processing_tasks >> final_task 