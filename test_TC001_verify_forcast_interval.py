import pytest
import logging
import re
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)

START_TIME = 0
DATE_TIME_REGEX_EXPR = '\\d{4}-\\d{2}-\\d{2}\\s\\d{2}:\\d{2}:\\d{2}'

def test_TC001_verify_days_of_data(response_value):

    logger.info("Starting of {}".format(__name__))
    global START_TIME
    try:
        logger.info("Verifying the interval of time in forecast data")
        for data in response_value["list"]:
            if re.match(DATE_TIME_REGEX_EXPR, data["dt_txt"]):
                date_time_str = re.match(DATE_TIME_REGEX_EXPR, data["dt_txt"]).group(0)
                date_time_object = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')
                if START_TIME == 0:
                    START_TIME = date_time_object
                else:
                    next_time = date_time_object
                    assert START_TIME + timedelta(hours=1) == next_time, "Failed to mismatch the time interval in " \
                                                                         "forcast data "
                    START_TIME = next_time
            else:
                logger.info("Format should not be {}".format(data))
                assert False

    except (RuntimeError, TypeError, NameError) as err:
        logger.debug("Exception thrown as :{}" + str(err))
        assert False

    logger.info("[Test Done] {}".format(__name__))
