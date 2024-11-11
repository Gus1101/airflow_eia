from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="second_dag",
    description="my second dag",
    start_date=datetime(2024, 11, 9),
    schedule="@daily",
    catchup=False
) as dag:

    task1 = BashOperator(task_id="task1", bash_command="sleep 5")
    task2 = BashOperator(task_id="task2", bash_command="sleep 5")
    task3 = BashOperator(task_id="task3", bash_command="sleep 5")

    # Using parallelism
    task1 >> [task2, task3]
