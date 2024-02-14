from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime, timedelta

# Common Parameters to intiate the operator
default_args = {
    "owner": "raghu",
    "retries": 5,
    "retry_delay": timedelta(minutes=5),
}

# Create an instance of DAG
with DAG(
    dag_id = "dag_with_postgres_operator", # id of dag
    description = "demo first dag", # description
    default_args = default_args, # default parameters of dag
    # parameters for start date and interval
    start_date = datetime(2024, 2, 1, 2), # start from 2024 feb 1 everyday at 2am
    schedule_interval = "@daily", # everyday
    catchup = False,

) as dag:
    task = PostgresOperator(
        task_id = "create_table_in_pg_db", # id of task
        postgres_conn_id = "postgres_db_connection", # connection id of postgres
        sql = "create table if not exists dag_runs (name varchar(50), age int);", # sql query
    )
    task2 = PostgresOperator(
        task_id = "insert_data_into_pg_db", # id of task
        postgres_conn_id = "postgres_db_connection", # connection id of postgres
        sql = "insert into dag_runs values('Raghu', 25);", # sql query
    )
    task >> task2