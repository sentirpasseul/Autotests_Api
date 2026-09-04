import logging
import os
import sys
from logging.handlers import RotatingFileHandler
from utils.logs.logger.logger_config import LoggerConfig


class Logger:
    __logger = None

    if not os.path.isdir(LoggerConfig.LOGS_DIR_NAME):
        os.makedirs(LoggerConfig.LOGS_DIR_NAME)
    __logger = logging.getLogger(LoggerConfig.LOGGER_NAME)
    __logger.setLevel(LoggerConfig.LOGS_LEVEL)
    __formatter = logging.Formatter(LoggerConfig.FORMAT)

    __console_handler = logging.StreamHandler()
    __console_handler.setFormatter(__formatter)
    __logger.addHandler(__console_handler)

    __file_handler = RotatingFileHandler(
        filename=LoggerConfig.LOGS_FILE_NAME,
        maxBytes=LoggerConfig.MAX_BYTES,
        backupCount=LoggerConfig.BACKUP_COUNT
    )
    __file_handler.setFormatter(__formatter)
    __logger.addHandler(__file_handler)

    @staticmethod
    def info(message: str):
        Logger.__logger.info(msg=message)

    @staticmethod
    def debug(message: str):
        Logger.__logger.debug(msg=message)

    @staticmethod
    def warning(message: str):
        Logger.__logger.warning(msg=message)

    @staticmethod
    def error(message: str):
        Logger.__logger.error(msg=message)

    @staticmethod
    def critical(message: str):
        Logger.__logger.critical(msg=message)
