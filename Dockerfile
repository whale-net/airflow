FROM apache/airflow:2.8.1

COPY --chown=airflow:root ./dags/ ${AIRFLOW_HOME}/dags/
