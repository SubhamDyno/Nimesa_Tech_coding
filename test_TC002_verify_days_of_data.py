import pytest
import logging
import re

logger = logging.getLogger(__name__)

DATE_REGEX_EXPR = "\\d{4}-\\d{2}-\\d{2}"
Date_dict = {}

def test_TC002_verify_days_of_data(response_value):

    logger.info("Starting of {}".format(__name__))
    try:
        logger.info("Analysing the text...")
        for index, data in enumerate(response_value["list"]):
            if re.match(DATE_REGEX_EXPR, data["dt_txt"]):
                date_str = re.match(DATE_REGEX_EXPR, data["dt_txt"]).group(0)
                Date_dict[date_str] = index
            else:
                logger.info("Date format is not proper in : {}\n".format(data))
                assert False

        logger.info("Verifying if response data contains 4 days of data and more")
        assert len(Date_dict) >= 4

    except (RuntimeError, TypeError, NameError) as err:
        logger.debug("Exception thrown as :{}" + str(err))
        assert False

    logger.info("[Test Done] {}".format(__name__))
