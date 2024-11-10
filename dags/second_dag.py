from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

dag = DAG(dag_id="first_dag",description="my first dag",
          start_date=datetime(2024,11,9),schedule_interval="@daily",
          catchup=False)

task1 = BashOperator(task_id="task1",bash_command="sleep 5",dag=dag)
task2 = BashOperator(task_id="task2",bash_command="sleep 5",dag=dag)
task3 = BashOperator(task_id="task3",bash_command="sleep 5",dag=dag)

#Using paralelism

task1 >> [task2,task3]