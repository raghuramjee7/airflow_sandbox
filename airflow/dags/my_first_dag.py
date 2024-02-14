from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

# Common Parameters to intiate the operator
default_args = {
    "owner": "raghu",
    "retries": 5,
    "retry_delay": timedelta(minutes=5),
}

# Create an instance of DAG
with DAG(
    dag_id = "my_first_dag_v1", # id of dag
    description = "demo first dag", # description
    default_args = default_args, # default parameters of dag
    # parameters for start date and interval
    start_date = datetime(2024, 2, 1, 2), # start from 2024 feb 1 everyday at 2am
    schedule_interval = "@daily", # everyday

) as dag:
    task1 = BashOperator(
        task_id = "first_task",
        bash_command = "echo This is the first task"
    )
    task2 = BashOperator(
        task_id = "second_task",
        bash_command = "echo This is the second task, this is run after the first task"
    )
    task3 = BashOperator(
        task_id = "thid_task",
        bash_command = "echo This is the third task, this is run after the first task, parallel to second task"
    )

    # This is one way to setup the dependencies
    # task1.set_downstream(task2)
    # task1.set_downstream(task3)

    # This is another way to setup the dependencies
    task1 >> task2
    task1 >> task3

    # This is the last way
    # task1 >> [task2, task3]

