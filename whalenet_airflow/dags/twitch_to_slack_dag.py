import asyncio
from datetime import datetime, timedelta

from airflow import DAG
from airflow.decorators import dag, task
from airflow.models.taskinstance import TaskInstance
from airflow.models.dagrun import DagRun

import sys
sys.path.append('/opt/airflow/dags/repo')
from whalenet_airflow.lib.twitch import get_connection_twitch, get_live_channels, live_channel_result

LIVE_CHECK_PERIOD = timedelta(minutes=5, hours=6)

#with DAG(dag_id='twitch_to_slack', start_date=datetime(2024, 1, 29), schedule="*/5 * * * *", catchup=False) as dag:

@dag(
    dag_id='twitch_to_slack', 
    start_date=datetime(2024, 1, 30), 
    schedule="@once",
    catchup=False,
)
def twitch_taskflow():

    @task()
    def get_twitch_channels():
        # TODO - eventually read from db or service
        channels_to_check = [
            'shadver',
            'summit1g',
            'shenanagans_',
        ]
        return channels_to_check

    @task()
    def get_live_twitch_channels(channel_names: list[str], task_instance: TaskInstance | None = None, dag_run: DagRun | None = None):

        twitch = asyncio.run(get_connection_twitch())
        
        print('dag_run.queued_at:', dag_run.queued_at)

        # TODO - grab current dag task start time or whatever i can get
        live_channel_results: list[live_channel_results] = asyncio.run(
            get_live_channels(twitch_connection=twitch, 
                              channel_logins=channel_names, 
                              live_grace_period=LIVE_CHECK_PERIOD,
                              live_as_of=dag_run.queued_at,
                              )
        ) 

        for res in live_channel_results:
            # TODO logger
            print(res)

        return live_channel_results

    # TODO store live results in airflow-common-db, and make more sophisticated decision around sending notification

    # @task()
    # def send_recently_live_to_slack():

    live_channels = get_live_twitch_channels(get_twitch_channels())
    # send_recently_live_to_slack(live_channels)

twitch_taskflow()