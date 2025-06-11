import requests, os
import pandas as pd
import xmltodict
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

resource_id = "16368672-ea58-419e-a8de-b36dec15f713"
API_URL = f"https://data.tmd.go.th/api/WeatherToday/V2/?uid=api&ukey=api12345"
headers = {
    "api-key": os.getenv("API_KEY")
}

def fetch_and_store():
    req = requests.get(API_URL)
    data_dict = xmltodict.parse(req.text)
    Stations = data_dict['WeatherToday']['Stations']['Station']
    df = pd.DataFrame(Stations)
    df.to_csv("raw.csv", index=False)

if __name__ == "__main__":
    fetch_and_store()