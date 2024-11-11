from airflow import DAG
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

with DAG(
    dag_id="dag_run_dag",
    description="dag that runs another dag",
    start_date=datetime(2024, 11, 9),
    schedule="@daily",
    catchup=False
) as dag:
    
    task1 = BashOperator(
        task_id="task1",
        bash_command="echo 'task1'"
    )

    trigger_child_dag = TriggerDagRunOperator(
        task_id="trigger_child_dag",
        trigger_dag_id="first_dag"
    )

    task1 >> trigger_child_dag