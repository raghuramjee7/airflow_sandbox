from airflow import DAG 
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator

def greet(name, age):
    print(f"My name is {name} and I am {age} years old")

default_args = {
    "owner": "raghu",
    "retries": 5,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id = "python_operator_dag_v1",
    description = "My DAG with python operator",
    default_args= default_args,
    start_date = datetime(2024, 2, 1, 2),
    schedule_interval = "@daily",
) as dag:
    task_1 = PythonOperator(
        task_id = "greet_fn",
        python_callable = greet,
        op_kwargs = {"name": "Raghu", "age": 22}
    )

    task_1