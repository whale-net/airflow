# whalenet_airflow
holds the dags for whalenet

## structure
This repo extends the apache airflow image by installing dependencies according to pyproject.toml. 
this is automatically deployed when a new build is published

the rest of our airflow deployment uses gitsync to sync whalenet_airflow module with the airflow server.
there is a dirty hack required to make this work, but it seems to work so we are rolling with it
```
# all dag files need this added to path to pickup library code in deployed airflow
import sys
sys.path.append('/opt/airflow/dags/repo')
```

Separating the dependencies and dag code means we do not need to redeploy with a new image every time we make a change.
not the safest pattern, but a convenient pattern

