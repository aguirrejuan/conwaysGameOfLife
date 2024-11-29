import sys
from pathlib import Path

from loguru import logger

default_log_dir = Path.home() / f".{__name__}" / "logs"
logger.add(default_log_dir / "running_logs.log", rotation="10 MB", retention="10 days")
logger.add(sys.stdout, level="INFO")
