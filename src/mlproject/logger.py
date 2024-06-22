import logging
import os
from datetime import datetime

#setting name to log file
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" 

# path where log file will be stored
log_path = os.path.join(os.getcwd(), "logs", LOG_FILE) 

# if log folder does not exists create one 
os.makedirs(log_path, exist_ok=True) 

LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

