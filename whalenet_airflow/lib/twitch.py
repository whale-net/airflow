from airflow.models import Variable
from twitchAPI.twitch import Twitch

channels_to_check = [
    'shadver',
    'summit1g'
]



def get_connection_twitch():
    return Twitch(Variable.get('TWITCH_API_APP_ID'), Variable.get('TWITCH_API_APP_SECRET'))




def get_live_channels():
    get_connection_twitch()