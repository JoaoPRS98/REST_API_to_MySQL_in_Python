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
  
  books = books_df.rename(columns={"asin": "product_id"}) #renaming column asin to product_id
  
  books["product_price"] = (books["product_price"]
                          .str.replace("$", "", regex=False) #removing $ sign
                          .str.replace(",", ".", regex=False) #replacing , with . if exist
                          .astype(float)) #converting to float
  
  books["product_original_price"] = (books["product_original_price"] #same this for original price
                                    .str.replace("$", "", regex=False)
                                    .str.replace(",", ".", regex=False)
                                    .astype(float))
  
books["discount_percentage"] = round((books["product_original_price"] - books["product_price"]) / books["product_original_price"] * 100, 2) #creating discount percentage column

books["product_byline"] = (books["product_byline"]
                           .str.replace("by ", "", regex=False)) #removing 'by ' from product_byline column

books = books.drop(columns=["book_formats"]) #dropping book_formats column (duplicate info)

books["product_byline_links"] = books["product_byline_links"].apply(lambda x: x[0]["link"] if isinstance(x, list) and len(x) > 0 else None) #extracting only the  byline link from product_byline_links list
books.head()
