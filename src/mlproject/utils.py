import os
import sys
from src.mlproject.exception import CustomeException
from src.mlproject.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql

# this will read .env file from directory
load_dotenv()

# this will read each infromation from .env file
host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db = os.getenv("db")

def read_sql_data():
    logging.info("Reading SQL database started")
    try:
        mydb = pymysql.connect(
            host=host,
            passwd=password,
            user=user,
            db=db
        )
        logging.info(f"Connection Established: {mydb}")

        df = pd.read_sql_query('SELECT * FROM students', mydb)
        print(df.head())

        return df
    except Exception as ex:
        raise CustomeException(ex)