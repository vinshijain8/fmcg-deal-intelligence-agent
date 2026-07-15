"""
relevance.py

Purpose:
---------
Filter only FMCG deal-related articles.

Input:
    data/cleaned_news.csv

Output:
    data/relevant_news.csv
"""

import os
import pandas as pd

# --------------------------------------------------
# Deal Keywords
# --------------------------------------------------

DEAL_KEYWORDS = [
    "acquisition",
    "acquire",
    "acquired",
    "merger",
    "merge",
    "merged",
    "buyout",
    "joint venture",
    "majority stake",
    "minority stake",
    "stake acquisition",
    "strategic investment in"
]

# --------------------------------------------------
# FMCG Keywords
# --------------------------------------------------

FMCG_KEYWORDS = [
    "fmcg",
    "consumer goods",
    "food",
    "foods",
    "beverage",
    "beverages",
    "snack",
    "snacks",
    "dairy",
    "bakery",
    "packaged food",
    "packaged foods",
    "personal care",
    "home care",
    "household products",

    # Companies
    "marico",
    "hul",
    "hindustan unilever",
    "dabur",
    "nestle",
    "nestlé",
    "britannia",
    "amul",
    "itc",
    "pepsico",
    "coca-cola",
    "coca cola",
    "godrej consumer",
    "gcpl",
    "colgate",
    "procter & gamble",
    "p&g",
    "dfm foods",
    "europastry",
    "parle",
    "mondelez",
    "unilever"
]

# --------------------------------------------------
# Exclude Keywords
# --------------------------------------------------

EXCLUDE_KEYWORDS = [
    "sensex",
    "nifty",
    "share price",
    "stock",
    "stocks",
    "stock market",
    "mutual fund",
    "earnings",
    "quarterly result",
    "quarterly results",
    "dividend",
    "brokerage",
    "target price",
    "analyst rating",
    "ipo",
    "forex",
    "currency",
    "bond",
    "interest rate",
    "fed",

    "bank",
    "banking",
    "insurance",

    "lawsuit",
    "attorney",
    "court",
    "litigation",

    "warner",
    "paramount",
    "bpcl",
    "coal india",
    "pnb",
    "tesla",
    "nvidia",
    "amd"
]


# --------------------------------------------------
# Relevance Function
# --------------------------------------------------

def is_relevant(title, description):

    title = str(title)
    description = str(description)

    text = (title + " " + description).lower()

    # Reject unwanted categories immediately
    if any(word in text for word in EXCLUDE_KEYWORDS):
        return False

    deal_found = any(word in text for word in DEAL_KEYWORDS)

    fmcg_found = any(word in text for word in FMCG_KEYWORDS)

    return deal_found and fmcg_found


# --------------------------------------------------
# Main Function
# --------------------------------------------------

def filter_relevant_news():

    INPUT_FILE = "data/cleaned_news.csv"
    OUTPUT_FILE = "data/relevant_news.csv"

    print("=" * 60)
    print("Filtering Relevant FMCG Deal News")
    print("=" * 60)

    df = pd.read_csv(INPUT_FILE)

    print(f"Articles before filtering : {len(df)}")

    relevant_articles = []

    for _, row in df.iterrows():

        title = row["Title"]
        description = row["Description"]

        if is_relevant(title, description):
            relevant_articles.append(row)

    relevant_df = pd.DataFrame(relevant_articles)

    relevant_df.reset_index(drop=True, inplace=True)

    os.makedirs("data", exist_ok=True)

    relevant_df.to_csv(OUTPUT_FILE, index=False)

    print(f"Articles after filtering : {len(relevant_df)}")

    print(f"\nSaved to {OUTPUT_FILE}")

    print("\nPreview\n")

    print(relevant_df.head())

    return relevant_df


if __name__ == "__main__":
    filter_relevant_news()