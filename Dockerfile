FROM apache/airflow:2.8.1

# using git sync
# COPY --chown=airflow:root ./dags/ ${AIRFLOW_HOME}/dags/

# should probably pin a python-specific version of airflow
RUN pip install -e .