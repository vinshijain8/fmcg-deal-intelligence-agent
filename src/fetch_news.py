"""
fetch_news.py

Purpose:
---------
1. Connect to NewsAPI
2. Download latest FMCG deal news
3. Convert JSON to a Pandas DataFrame
4. Save raw data as CSV
"""

import os
import requests
import pandas as pd
from dotenv import load_dotenv


def fetch_news():
    # -------------------------------------------------------
    # Load environment variables (.env)
    # -------------------------------------------------------
    load_dotenv()

    NEWS_API_KEY = os.getenv("NEWS_API_KEY")

    if not NEWS_API_KEY:
        raise ValueError("NEWS_API_KEY not found in .env file")

    # -------------------------------------------------------
    # NewsAPI endpoint
    # -------------------------------------------------------
    URL = "https://newsapi.org/v2/everything"

    # Multiple search queries for better coverage
    queries = [
        "FMCG acquisition",
        "FMCG merger",
        "FMCG investment",
        "consumer goods acquisition",
        "food company acquisition",
        "beverage company acquisition"
    ]

    all_articles = []

    print("=" * 60)
    print("Fetching news from NewsAPI...")
    print("=" * 60)

    # -------------------------------------------------------
    # Fetch articles for every query
    # -------------------------------------------------------
    for query in queries:

        print(f"\nSearching: {query}")

        params = {
            "q": query,
            "language": "en",
            "sortBy": "publishedAt",
            "pageSize": 20,
            "apiKey": NEWS_API_KEY
        }

        response = requests.get(URL, params=params)

        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            continue

        data = response.json()

        articles = data.get("articles", [])

        print(f"Found {len(articles)} articles")

        for article in articles:

            all_articles.append({
                "Title": article.get("title"),
                "Description": article.get("description"),
                "Source": article.get("source", {}).get("name"),
                "PublishedAt": article.get("publishedAt"),
                "URL": article.get("url")
            })

    # -------------------------------------------------------
    # Convert to DataFrame
    # -------------------------------------------------------
    df = pd.DataFrame(all_articles)

    # -------------------------------------------------------
    # Remove exact duplicate URLs
    # -------------------------------------------------------
    df.drop_duplicates(subset="URL", inplace=True)

    # -------------------------------------------------------
    # Create data folder if it doesn't exist
    # -------------------------------------------------------
    os.makedirs("data", exist_ok=True)

    # -------------------------------------------------------
    # Save CSV
    # -------------------------------------------------------
    output_path = "data/raw_news.csv"

    df.to_csv(output_path, index=False)

    print("\n" + "=" * 60)
    print(f"Total unique articles: {len(df)}")
    print(f"Saved to: {output_path}")
    print("=" * 60)

    print("\nFirst 5 Articles\n")
    print(df.head())

    return df


if __name__ == "__main__":
    fetch_news()