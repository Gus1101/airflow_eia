from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

dag = DAG(
    dag_id="second_dag",
    description="my second dag",
    start_date=datetime(2024, 11, 9),
    schedule="@daily",
    catchup=False
)

task1 = BashOperator(task_id="task1", bash_command="sleep 5", dag=dag)
task2 = BashOperator(task_id="task2", bash_command="sleep 5", dag=dag)
task3 = BashOperator(task_id="task3", bash_command="sleep 5", dag=dag)

# Using parallelism
task1 >> [task2, task3]
