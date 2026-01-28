import logging
import os
from datetime import datetime
from logging.handlers import RotatingFileHandler

# Create logs directory if it doesn't exist
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)

# Generate log file name with timestamp
LOG_FILE_PATH = os.path.join(logs_dir, f"ml_project_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")

# Configure logger with RotatingFileHandler
logger = logging.getLogger('ml_project')
logger.setLevel(logging.DEBUG)

# File handler (detailed logging)
file_handler = RotatingFileHandler(
    LOG_FILE_PATH,
    maxBytes=10485760,  # 10MB
    backupCount=5
)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter(
    '[%(asctime)s] - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
))

# Console handler (simple logging)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter(
    '[%(asctime)s] - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
))

# Add handlers
if not logger.handlers:
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

def get_logger():
    """Returns the configured logger instance."""
    return logger
