from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

dag = DAG(
    dag_id="third_dag",
    description="my third dag",
    start_date=datetime(2024, 11, 9),
    schedule="@daily",
    catchup=False
)

task1 = BashOperator(task_id="task1", bash_command="sleep 5", dag=dag)
task2 = BashOperator(task_id="task2", bash_command="sleep 5", dag=dag)
task3 = BashOperator(task_id="task3", bash_command="sleep 5", dag=dag)

# Exploring Precedence
task1 >> task3
task2 >> task3
