# airflow_sandbox

Airflow sandbox for practise

## Setup

1. Create a git directoty for practise and clone it
2. Create a pipenv environment and install req dependencies - `pipenv install --python=3.7 Flask==1.0.3 apache-airflow==1.10.3`
3. We setup airflow home dir in an env file - `echo "AIRFLOW_HOME=${PWD}/airflow" >> .env`
4. Airflow req a db to run, by default it uses a sqlite db for this process - `airflow initdb`
5. Then we create a folder to setup our dags - `mkdir -p ${AIRFLOW_HOME}/dags/`
6. Run airflow - `airflow webserver -p 8081`
7. Start airflow scheduler - `airflow scheduler`
8. Run task from a dag - `airflow run <dag> <task> 2020-05-31`
9. List tasks in a dag - `airflow list_tasks <dag>`
10. Pause and unpause dag - `airflow pause/unpause <dag>`
11. 
