from airflow.decorators import dag, task
from datetime import datetime, timedelta

default_args = {
    "owner": "raghu",
    "retries": 5,
    "retry_delay": timedelta(minutes=5),
}

# we use the dag decorator to define the DAG
@dag(
    dag_id = "taskflow_api_dag_v1",
    description = "My DAG with taskflow api",
    default_args= default_args,
    start_date = datetime(2024, 2, 1, 2),
    schedule_interval = "@daily",
)
def hello_world_etl():
    
    # we use the task decorator to define the task
    # we define that multiple outputs are returned here
    @task(multiple_outputs = True)
    def get_name():
        return {
            "first_name": "raghu",
            "last_name": "ramjee"
        }

    @task()
    def get_age():
        return 22
    
    @task()
    def greet(first_name, last_name, age):
        print(f"My name is {first_name} {last_name} and I am {age} years old")
        
    name = get_name()
    age = get_age()
    greet(first_name=name["first_name"], 
          last_name=name["last_name"], 
          age=age)

greet_dag = hello_world_etl()