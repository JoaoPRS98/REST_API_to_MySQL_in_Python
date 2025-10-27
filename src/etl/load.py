"""
load.py
--------

This module handles the load phase of the ETL process.
It connects to a MySQL database using credentials from environment variables
and loads the transformed pandas DataFrame into the target table.

Connection details are securely stored in the .env file:
- MYSQL_HOST
- MYSQL_PORT
- MYSQL_USER
- MYSQL_PASSWORD
- MYSQL_DB
"""


#imports
import os
import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
from transform import transform_data
from dotenv import load_dotenv


#load environment variables
load_dotenv()

#credentials from .env file
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_PORT = os.getenv("MYSQL_PORT")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DB = os.getenv("MYSQL_DB")


def load_to_mysql(df):
    """
    Loads the transformed DataFrame into a MySQL table.
    Appends the data to the existing table if it already exists.
    """

    try:
        #create engine
        engine = create_engine(
            f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}"
        )

        #load data into MySQL table
        df.to_sql(name="amazon_books", con=engine, if_exists="append", index=False)

        print("Data inserted successfully into MySQL!")

    except Exception as e:
        print(f"Error loading data into MySQL: {e}")
