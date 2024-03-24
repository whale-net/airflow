import asyncio
from datetime import datetime, timedelta, timezone

from airflow import DAG
from airflow.decorators import dag, task
from airflow.models.variable import Variable
from airflow.models.taskinstance import TaskInstance
from airflow.models.dagrun import DagRun


import sys
sys.path.append('/opt/airflow/dags/repo')
from whalenet_airflow.lib.twitch import get_connection_twitch, get_live_channels, LiveChannelResult
from whalenet_airflow.lib.slack import get_client, send_message

LIVE_CHECK_PERIOD = timedelta(minutes=2)

@dag(
    dag_id='twitch_to_slack', 
    start_date=datetime(2024, 3, 24), 
    schedule_interval=LIVE_CHECK_PERIOD,
    catchup=False,
)
def twitch_taskflow():

    @task()
    def get_twitch_channels():
        # TODO - eventually read from db or service
        channels_to_check = [
            'shadver',
            'moomasterq',
            'noodlesruns',
            'kingcolony',
        ]
        return channels_to_check

    @task()
    def get_live_twitch_channels(channel_names: list[str], task_instance: TaskInstance | None = None, dag_run: DagRun | None = None):

        twitch = asyncio.run(get_connection_twitch())
        
        print('dag_run.queued_at:', dag_run.queued_at)

        # TODO - grab current dag task start time or whatever i can get
        live_channel_results: list[LiveChannelResult] = asyncio.run(
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
    
    @task()
    def send_recently_live_to_slack(live_channels: list[LiveChannelResult]):
        if len(live_channels) == 0:
            print('no channels live')
            return
        
        header = "Recently Live Twitch Channels"
        body_parts: list[str] = []

        current_time = datetime.now(tz=timezone.utc)
        url_base = f"https://twitch.tv/"
        for result in live_channels:
            start_diff =  current_time - result.started_at
            target_url = url_base + result.login_name
            # i guess this don't work yet
            body_msg = f"- {result.display_name} went live @ {target_url} ({start_diff.total_seconds()} seconds ago)"
            body_parts.append(body_msg)

        final_message_list = [header, *body_parts]
        final_msg = '\n'.join(final_message_list)
        
        slack_client = get_client()
        slack_channel_id = Variable.get('TWITCH_ALERT_SLACK_CHANNEL_ID')
        send_message(slack_client, slack_channel_id, message=final_msg)



    # TODO store live results in airflow-common-db, and make more sophisticated decision around sending notification

    # @task()
    # def send_recently_live_to_slack():

    live_channels = get_live_twitch_channels(get_twitch_channels())
    send_recently_live_to_slack(live_channels)

twitch_taskflow()