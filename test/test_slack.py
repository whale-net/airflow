import os
import asyncio
from unittest.mock import patch

import pytest

from whalenet_airflow.lib.slack import get_client, get_channels, send_message

@pytest.mark.skipif('SLACK_WHALEBOT_OAUTH_TOKEN' not in os.environ, reason='NOT CI - only run if have api key')
def test_slack_connection():
    with patch.dict('os.environ', {
                    'AIRFLOW_VAR_SLACK_WHALEBOT_OAUTH_TOKEN': os.environ.get('SLACK_WHALEBOT_OAUTH_TOKEN'),
                }):
        
        client = get_client()

    assert client

@pytest.mark.skipif('SLACK_WHALEBOT_OAUTH_TOKEN' not in os.environ or 'TWITCH_ALERT_SLACK_CHANNEL_ID' not in os.environ, reason='NOT CI - only run if have api key')
def test_slack_dev():
    """
    using this test as an entrypoint for local development
    """

    with patch.dict('os.environ', {
                    'AIRFLOW_VAR_SLACK_WHALEBOT_OAUTH_TOKEN': os.environ.get('SLACK_WHALEBOT_OAUTH_TOKEN'),
                }):
        
        client = get_client()
        #channels = get_channels(client)
        send_message(client, channel_id=os.environ.get('TWITCH_ALERT_SLACK_CHANNEL_ID'), message="hello from test (again)")
