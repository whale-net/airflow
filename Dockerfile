FROM apache/airflow:2.8.3-python3.11

ARG ENV=dev

# should probably pin a python-specific version of airflow
COPY pyproject.toml ${AIRFLOW_HOME}
RUN pip install -e .[deploy]

# using git sync - but still copying over in non-deploy environments for easier debug
RUN mkdir ${AIRFLOW_HOME}/dag_stage
COPY --chown=airflow:root ./whalenet_airflow ${AIRFLOW_HOME}/dag_stage/
RUN if [ "$ENV" != "deploy" ] ; then mv ${AIRFLOW_HOME}/dag_stage/ ${AIRFLOW_HOME}/dags/whalenet_airflow ; fi
RUN rm -rf ${AIRFLOW_HOME}/dag_stage

# make all of our classes serializable
# not universally true but whatever
ENV AIRFLOW__CORE__ALLOWED_DESERIALIZATION_CLASSES="airflow.* whalenet_airflow.*"
