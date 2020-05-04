import pytest
import logging

logger = logging.getLogger(__name__)

def test_TC003_verify_temp_range(response_value):

    logger.info("Starting of {}".format(__name__))
    try:
        logger.info("Comparing temperature in proper order")
        for temp in response_value["list"]:
            if temp["main"]["temp_min"] <= temp["main"]["temp"] <= temp["main"]["temp_max"]:
                assert True
            else:
                logger.info("Temperature value should be Temp_min <= Temp <= Temp_max, "
                            "but here {} {} {}".format(temp["main"]["temp_min"], temp["main"]["temp"], temp["main"]["temp_max"]))
                assert False

    except (RuntimeError, TypeError, NameError) as err:
        logger.debug("Exception thrown as :{}" + str(err))
        assert False

    logger.info("[Test Done] {}".format(__name__))
