from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

dag = DAG(
    dag_id="fourth_dag1",
    description="my fourth dag",
    start_date=datetime(2024, 11, 9),
    schedule="@daily",
    catchup=False
)

task1 = BashOperator(task_id="task1", bash_command="sleep 5", dag=dag)
task2 = BashOperator(task_id="task2", bash_command="sleep 5", dag=dag)
task2 = BashOperator(task_id="task3", bash_command="sleep 5", dag=dag)
task2 = BashOperator(task_id="task4", bash_command="sleep 5", dag=dag)
task2 = BashOperator(task_id="task5", bash_command="sleep 5", dag=dag)
task2 = BashOperator(task_id="task6", bash_command="exit 1", dag=dag)
task2 = BashOperator(task_id="task7", bash_command="sleep 5", dag=dag)
task2 = BashOperator(task_id="task8", bash_command="sleep 5", dag=dag)
task3 = BashOperator(task_id="task9", bash_command="sleep 5", dag=dag,
                     trigger_rule = "one_failed")

# Exploring Precedence
task1 >> task2
task3 >> task4
[task2, task4] >> task5 >> task6
task6 >> [task7, task8, task9]