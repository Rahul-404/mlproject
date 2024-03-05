import logging
import os
from datetime import datetime

# log file content
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# where excatly log file will be saved = cuttent directory + "logs %m_%d_%Y_%H_%M_%S"
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)

# will create directory using above path, there log data will be stored
os.makedirs(logs_path, exist_ok=True)

# saving log file to exact location
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

