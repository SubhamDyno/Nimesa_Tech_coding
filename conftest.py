import requests
import json
import pytest
import logging

logger = logging.getLogger(__name__)

URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

@pytest.fixture
def response_value():
    logger.debug("Fixture started")
    payload = {}
    headers = {}
    response = requests.request("GET", URL, headers=headers, data=payload)

    if response.status_code != 200:
        logger.info("Error in response code {}".format(response.status_code))
        return False
    else:
        logger.info("Response {} received".format(response.status_code))
        response = json.loads(response.text)
        logger.debug("Fixture Done")
        return response
