import logging
from pathlib import Path


class LoggerConfig:
    PROJECT_ROOT = Path(__file__).resolve().parents[3]
    LOGS_DIR_NAME = PROJECT_ROOT / "artifacts" / "logs"
    LOGGER_NAME = "Logger"
    LOGS_FILE_NAME = LOGS_DIR_NAME / "test.log"
    LOGS_LEVEL = logging.INFO
    MAX_BYTES = 100000
    BACKUP_COUNT = 10
    FORMAT = "\n[%(asctime)s - %(levelname)s] - %(message)s"
    DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%S'
