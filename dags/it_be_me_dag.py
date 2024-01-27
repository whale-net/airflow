from datetime import datetime

from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator

#with DAG(dag_id='test_dag', start_date=datetime(2024, 1, 27), schedule="* * * * *"):
with DAG(dag_id='yar_be_the_dag', start_date=datetime(2024, 1, 27), schedule="* * * * *") as dag:

    @task()
    def sample_python_task():
        print('this was printed from a python task')

    @task()
    def sample_python_task_2():
        print('this was printed from a python task that ran after the test_operator')


    sample_python_task() >> sample_python_task_2()
