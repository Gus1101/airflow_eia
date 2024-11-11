from airflow import DAG
from airflow.operators.dagrun_operator import TriggerDagRunOperator
from datetime import datetime

with DAG(
    dag_id="dag_run_dag",
    description="my third dag",
    start_date=datetime(2024, 11, 9),
    schedule="@daily",
    catchup=False
) as dag:

    trigger_child_dag = TriggerDagRunOperator(
        task_id="trigger_child_dag",
        trigger_dag_id="task_group_dag",
        wait_for_completition=True,
        reser_dag_run=False
    )