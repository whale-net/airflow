# whalenet_airflow
holds the dags for whalenet

## structure
This repo extends the apache airflow image by installing dependencies according to pyproject.toml. this is automatically deployed

the rest of our airflow deployment uses gitsync to sync whalenet_airflow module with the airflow server.

Separating the dependencies and dag code means we do not need to redeploy with a new image every time we make a change.

