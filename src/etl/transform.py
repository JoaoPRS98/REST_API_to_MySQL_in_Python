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

  books_df = pd.DataFrame(data)

  #renaming column asin to product_id
  books = books_df.rename(columns={"asin": "product_id"}) 

  #price cleaning and conversion
  books["product_price"] = (books["product_price"]
                          .str.replace("$", "", regex=False) #removing $ sign
                          .str.replace(",", ".", regex=False) #replacing , with . if exist
                          .astype(float)) #converting to float

  #price cleaning and conversion
  books["product_original_price"] = (books["product_original_price"] #same this for original price
                                    .str.replace("$", "", regex=False)
                                    .str.replace(",", ".", regex=False)
                                    .astype(float))
  #creating discount percentage column
  books["discount_percentage"] = round((books["product_original_price"] - books["product_price"]) / books["product_original_price"] * 100, 2) 

  #removing 'by ' from product_byline column
  books["product_byline"] = (books["product_byline"]
                           .str.replace("by ", "", regex=False)) 
  
  #dropping book_formats column (duplicate info)
  books = books.drop(columns=["book_formats"]) 

  #extracting only the  byline link from product_byline_links list
  books["product_byline_links"] = books["product_byline_links"].apply(lambda x: x[0]["link"] if isinstance(x, list) and len(x) > 0 else None) 
  books.head()
