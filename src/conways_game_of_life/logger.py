import os
import sys
import logging
from pathlib import Path
from logging.handlers import RotatingFileHandler

PROJECT_NAME = "conways-game-of-life"

# Allow the log directory to be configurable via an environment variable
default_log_dir = Path.home() / f".{PROJECT_NAME}" / "logs"
log_dir = Path(os.getenv("RECAPTURE_LOG_DIR", default_log_dir))

log_filepath = log_dir / "running_logs.log"
os.makedirs(log_dir, exist_ok=True)

logging_str = f"[%(asctime)s: {PROJECT_NAME}: %(levelname)s: %(module)s: %(message)s]"

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        RotatingFileHandler(log_filepath, maxBytes=10485760, backupCount=5),
        logging.StreamHandler(sys.stdout),
    ],
)

logger = logging.getLogger(PROJECT_NAME)