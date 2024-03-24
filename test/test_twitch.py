import os
import asyncio
from unittest.mock import patch

from twitchAPI.type import AuthScope

import pytest

from whalenet_airflow.lib.twitch import get_connection_twitch, get_live_channels

# @patch('whalenet_airflow.lib.twitch.Variable')
# @pytest.mark.skipif('TWITCH_API_APP_ID' not in os.environ, reason='only run if have api key')
# def test_twitch(variable):
#     variable = {
#         'TWITCH_API_APP_ID': os.environ.get('TWITCH_API_APP_ID'),
#         'TWITCH_API_APP_SECRET': os.environ.get('TWITCH_API_APP_SECRET'),
#     }
#     conn = get_connection_twitch()

@pytest.mark.skipif('TWITCH_API_APP_ID' not in os.environ, reason='only run if have api key')
def test_twitch():
    with patch.dict('os.environ', {
                    'AIRFLOW_VAR_TWITCH_API_APP_ID': os.environ.get('TWITCH_API_APP_ID'),
                    'AIRFLOW_VAR_TWITCH_API_APP_SECRET': os.environ.get('TWITCH_API_APP_SECRET'),
                }):
        #scopes = []
        conn = asyncio.run(get_connection_twitch())

        channels = [
            'shadver',
            'summit1g',
            'shenanagans_',
            'gorgc',
        ]
        results = asyncio.run(get_live_channels(conn, channel_logins=channels))
    assert len(results) > 0

