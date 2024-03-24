from airflow.models.variable import Variable
from slack_sdk import WebClient
from slack_sdk.web import SlackResponse



def get_client() -> WebClient:
    client = WebClient(token=Variable.get('SLACK_WHALEBOT_OAUTH_TOKEN'))
    
    # will raise SlackApiError
    client.auth_test()

    return client

def get_channels(client: WebClient) -> SlackResponse:
    return client.conversations_list()

def send_message(client: WebClient, channel_id: str, message: str):
    # TODO - consider using blocks - seems better
    client.chat_postMessage(channel=channel_id, text=message)

