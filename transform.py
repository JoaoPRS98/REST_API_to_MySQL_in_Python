from extract import extract_api_data
import pandas as pd

json_data = extract_api_data()

products = json_data["data"]["products"]
df = pd.json_normalize(products)
print(df.head())
