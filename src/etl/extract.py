"""
extract.py
-----------

This module is responsible for extracting product data from the RapidAPI
Real-Time Amazon Data API. It retrieves product information based on
a specific category (in this case, books) and returns the data as JSON.

The extracted data will later be transformed and loaded into a MySQL database
as part of the ETL pipeline.
"""

# Imports
import json
import requests
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("API_KEY")
API_HOST = os.getenv("API_HOST")

def extract_api_data():
    #getting data of amazon data from rapidapi
    url = "https://real-time-amazon-data.p.rapidapi.com/products-by-category"

    #setting key and host in headers
    headers = {
        "X-RapidAPI-Key": API_KEY, #defined in .env file
        "X-RapidAPI-Host": API_HOST #defined in .env file
    }

    #getting the category books
    params = {"category_id": category_id}

    response = requests.get(url, headers=headers, params=params)
    json_data = response.json()

    #checking if the response is successful
    if response.status_code == 200:
        print("Data extracted successfully!")
    else:
        print(f"Failed to extract data. Status code: {response.status_code}")
    return json_data
