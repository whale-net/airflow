import os
from unittest.mock import patch

import pytest

from whalenet_airflow.lib.twitch import get_connection_twitch

@patch('whalenet_airflow.lib.twitch.Variable')
@pytest.mark.skipif('TWITCH_API_APP_ID' not in os.environ, reason='only run if have api key')
def test_twitch(variable):
    variable = {
        'TWITCH_API_APP_ID': os.environ.get('TWITCH_API_APP_ID'),
        'TWITCH_API_APP_SECRET': os.environ.get('TWITCH_API_APP_SECRET'),
    }
    conn = get_connection_twitch()
    print(conn)
