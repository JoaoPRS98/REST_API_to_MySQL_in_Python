import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from etl.extract import extract_api_data
from etl.transform import transform_books_data
from etl.load import load_to_mysql


def main():
    print("Starting ETL process...")

    #extract
    print("Extracting data from API...")
    json_data = extract_api_data()
    print("Data extracted successfully.")

    #transform
    print("Transforming data...")
    books = transform_books_data(json_data)
    print("Data transformed successfully.")

    #load
    print("Loading data into MySQL...")
    load_to_mysql(books)
    print("Data loaded successfully.")

    print("ETL process completed")
