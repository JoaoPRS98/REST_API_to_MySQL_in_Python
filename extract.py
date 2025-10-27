#imports
import json
import requests

#remover depois
API_KEY = "8c54ca9e46msh8eefe6b139cd3b9p1a8b28jsna71252a67483"
API_HOST = "real-time-amazon-data.p.rapidapi.com"

def extract_api_data():
    #getting data of amazon data from rapidapi
    url = "https://real-time-amazon-data.p.rapidapi.com/products-by-category"

    #setting key and host in headers
    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": API_HOST
    }

    #getting the category books
    params = {"category_id":"283155"}

    response = requests.get(url, headers=headers, params=params)
    json_data = response.json()

    #checking if the response is successful
    if response.status_code == 200:
        print("Data extracted successfully!")
    else:
        print(f"Failed to extract data. Status code: {response.status_code}")
    return json_data
print(extract_api_data())

