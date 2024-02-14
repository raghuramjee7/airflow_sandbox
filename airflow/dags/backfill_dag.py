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
    dag_id = "backfill_practise_dag", # id of dag
    description = "dag to test backfilling", # description
    default_args = default_args, # default parameters of dag
    # parameters for start date and interval
    start_date = datetime(2024, 2, 1, 2), # start from 2024 feb 1 everyday at 2am
    schedule_interval = "@daily", # everyday
    catchup = False,

) as dag:
    task1 = BashOperator(
        task_id = "first_task",
        bash_command = "echo This is the first task"
    )

