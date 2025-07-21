import logging
import os

assert 'TOKEN' in os.environ


def log_level() -> int:
    """
    LOG_LEVEL

    Type: int
    Default: logging.INFO
    Description: Logging level
    """
    return int(os.environ.get('LOG_LEVEL', logging.INFO))


def token() -> str:
    """
    BOT_TOKEN (Required)

    Type: str
    Description: Bot token
    """
    return os.environ['TOKEN']
