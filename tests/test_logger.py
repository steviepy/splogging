import logging

from splogging import logger


def test_logger_type():
    logger1 = logger.setup_logging(name="logger1")
    assert isinstance(logger1, logging.Logger)


def test_logger_number_of_handlers():
    logger2 = logger.setup_logging(name="logger2")
    assert len(logger2.handlers) == 2
    logger3 = logger.setup_logging(name="logger3", console_level=None)
    assert len(logger3.handlers) == 1
    logger4 = logger.setup_logging(name="logger4", file_level=None)
    assert len(logger4.handlers) == 1
