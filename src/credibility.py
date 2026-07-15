"""
credibility.py

Purpose:
---------
Assign credibility scores to news articles.

Input:
    data/deduplicated_news.csv

Output:
    data/scored_news.csv
"""

import pandas as pd


TRUSTED_SOURCES = {
    "Reuters": 10,
    "Bloomberg": 10,
    "The Economic Times": 9,
    "The Times of India": 9,
    "BusinessLine": 8,
    "Mint": 8,
    "Moneycontrol": 8,
    "CNBC": 9,
    "Livemint": 8,
    "News18": 7,
    "Yahoo Entertainment": 6
}


def get_score(source):
    source = str(source)

    for trusted, score in TRUSTED_SOURCES.items():
        if trusted.lower() in source.lower():
            return score

    return 5


def score_news():

    INPUT_FILE = "data/deduplicated_news.csv"
    OUTPUT_FILE = "data/scored_news.csv"

    print("=" * 60)
    print("Scoring News Credibility")
    print("=" * 60)

    df = pd.read_csv(INPUT_FILE)

    print(f"Articles before scoring: {len(df)}")

    df["Credibility"] = df["Source"].apply(get_score)

    df = df.sort_values(
        by="Credibility",
        ascending=False
    )

    df.to_csv(OUTPUT_FILE, index=False)

    print("\nPreview\n")
    print(df.head())

    print(f"\nSaved {OUTPUT_FILE}")

    return df


if __name__ == "__main__":
    score_news()