"""
transform.py
------------

This module handles the transformation phase of the ETL process.
It takes the raw JSON data extracted from the RapidAPI Amazon Data API,
cleans and standardizes it using pandas, and prepares it for loading
into a MySQL database.

Transformations performed:
- Rename columns for consistency
- Clean and convert prices from string to float
- Calculate discount percentage
- Simplify 'product_byline' and 'product_byline_links' fields
- Drop unnecessary or nested columns
"""

# Imports
import pandas as pd
from extract import extract_api_data

def transform_data():
  json_data = extract_api_data()
  data = json_data["data"]["products"]
