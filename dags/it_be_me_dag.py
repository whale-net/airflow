import time
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

    @task()
    def sample_python_task_3():
        print('this was printed from a python task that ran after the test_operator')

    @task()
    def sample_python_task_4():
        print('this was printed from a python task that ran after the test_operator')

    @task()
    def sample_python_task_5():
        print('this was printed from a python task that ran after the test_operator')
        time.sleep(15)
        print('haha, waited')

    @task()
    def sample_python_task_6():
        print('this was printed from a python task that ran after the test_operator')

    @task()
    def sample_python_task_7():
        print('this was printed from a python task that ran after the test_operator')

    @task()
    def sample_python_task_8():
        print('this was printed from a python task that ran after the test_operator')

    @task()
    def sample_python_task_9():
        print('this was printed from a python task that ran after the test_operator')

    @task()
    def sample_python_task_10():
        print('this was printed from a python task that ran after the test_operator')

    @task()
    def sample_python_task_11():
        print('this was printed from a python task that ran after the test_operator')

    @task()
    def sample_python_task_12():
        print('this was printed from a python task that ran after the test_operator')

    @task()
    def sample_python_task_13():
        print('this was printed from a python task that ran after the test_operator')

    @task()
    def sample_python_task_14():
        print('this acts as a collector task of sorts')

    @task()
    def sample_python_task_15():
        print('this was printed from a python task that ran after the test_operator and is the last task')


    #sample_python_task() >> sample_python_task_2() >> sample_python_task_9() >> [sample_python_task_3(), sample_python_task_4()] >> sample_python_task_8()


    t2 = sample_python_task_2()
    t3 = sample_python_task_3()
    t4 = sample_python_task_4()

    intro_chain = sample_python_task() >> t2 >> sample_python_task_9()
    divergent_1 = t2 >> [t3, t4, sample_python_task_5()] >> sample_python_task_6() >> sample_python_task_7()

    divergent_2 = [t3, t4, intro_chain] >> sample_python_task_8()

    sub_divergent = divergent_2 >> [sample_python_task_10(), sample_python_task_11(), sample_python_task_12(), sample_python_task_13()] >> sample_python_task_14()

    [divergent_1, sub_divergent] >> sample_python_task_15()
