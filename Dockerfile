FROM apache/airflow:2.8.1

COPY ./dags/ \${AIRFLOW_HOME}/dags/

