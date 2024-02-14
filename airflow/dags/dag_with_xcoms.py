from airflow import DAG 
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator

def greet(ti):
    # pull data from ti
    name = ti.xcom_pull(task_ids = "get_name", key = "name")
    age = ti.xcom_pull(task_ids = "get_age", key = "age")

    print(f"My name is {name} and I am {age} years old")

def returns_name(ti):
    # we can simply return like this return {"name": "Raghu"}
    # push data
    ti.xcom_push(key="name", value="Raghu")

def returns_age(ti):
    # push data
    ti.xcom_push(key="age", value=22)

default_args = {
    "owner": "raghu",
    "retries": 5,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id = "python_xcom_dag_v1",
    description = "My DAG with xcoms",
    default_args= default_args,
    start_date = datetime(2024, 2, 1, 2),
    schedule_interval = "@daily",
) as dag:
    task_1 = PythonOperator(
        task_id = "get_name",
        python_callable = returns_name,
    )
    task_2 = PythonOperator(
        task_id = "get_age",
        python_callable = returns_age,
    )
    task_3 = PythonOperator(
        task_id = "greet",
        python_callable = greet,
    )

    [task_1, task_2] >> task_3