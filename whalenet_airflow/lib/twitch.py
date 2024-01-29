from airflow.models import Variable
from twitchAPI.twitch import Twitch

channels_to_check = [
    'shadver',
    'summit1g'
]

def get_live_channels():

    app_id = Variable.get('twitch_app_id')
    app_secret = Variable.get('twitch_app_secret')
    twitch = Twitch(app_id, app_secret)