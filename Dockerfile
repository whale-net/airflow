FROM apache/airflow:2.8.1-python3.11

ARG ENV=dev

# should probably pin a python-specific version of airflow
COPY pyproject.toml ${AIRFLOW_HOME}
RUN pip install -e .

# using git sync - but still copying over in non-deploy environments for easier debug
RUN mkdir ${AIRFLOW_HOME}/dag_stage
COPY --chown=airflow:root ./dags/ ${AIRFLOW_HOME}/dag_stage/
RUN if [ "$ENV" != "deploy" ] ; then mv ${AIRFLOW_HOME}/dag_stage/* ${AIRFLOW_HOME}/dags ; fi
RUN rm -rf ${AIRFLOW_HOME}/dag_stage


