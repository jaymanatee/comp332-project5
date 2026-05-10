import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_top_headlines(country="us", limit=10):
    """Fetch top news headlines from NewsAPI."""
    api_key = os.getenv("NEWSAPI_KEY")
    
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "country": country,
        "pageSize": limit,
        "apiKey": api_key
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    # Extract just the titles
    titles = [article["title"] for article in data["articles"] if article["title"]]
    return titles

if __name__ == "__main__":
    print(get_top_headlines())