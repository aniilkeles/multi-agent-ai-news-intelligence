import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("NEWS_API_KEY")

def search_news(topic):

    url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={API_KEY}"

    response = requests.get(url)
    data = response.json()

    articles = []

    for article in data["articles"][:5]:

        title = article["title"]
        description = article["description"]

        articles.append(f"{title} - {description}")

    return articles