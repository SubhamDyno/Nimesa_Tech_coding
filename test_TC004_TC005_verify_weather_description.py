import pytest
import logging

logger = logging.getLogger(__name__)


@pytest.mark.parametrize("id_value, desc_value", [(800, 'clear sky'), (500, 'light rain')])
def test_TC001_verify_weather_description(response_value, id_value, desc_value):
    logger.info("Starting of {} with id {}".format(__name__, id_value))
    try:
        logger.info("Checking id:{} with description :{}".format(id_value, desc_value))
        for each_label in response_value["list"]:
            if each_label["weather"][0]["id"] == id_value:
                assert each_label["weather"][0]["description"] == desc_value
            else:
                pass

    except (RuntimeError, TypeError, NameError) as err:
        logger.debug("Exception thrown as :{}" + str(err))
        assert False

    logger.info("Starting of {}".format(__name__))
