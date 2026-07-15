"""
newsletter.py

Purpose:
---------
Generate an FMCG newsletter using Gemini.

Input:
    data/scored_news.csv

Output:
    output/newsletter.md
"""

import os
import pandas as pd
from dotenv import load_dotenv
from google import genai


def generate_newsletter():

    load_dotenv()

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    if not GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY not found.")

    client = genai.Client(api_key=GEMINI_API_KEY)

    INPUT_FILE = "data/scored_news.csv"

    df = pd.read_csv(INPUT_FILE)

    articles = ""

    for i, row in df.iterrows():

        articles += f"""
Article {i+1}

Title:
{row['Title']}

Description:
{row['Description']}

Source:
{row['Source']}

Credibility:
{row['Credibility']}
"""

    prompt = f"""
You are an FMCG industry analyst.

Using the articles below, generate a concise professional newsletter.

For every article provide:

Company:
Deal Type:
Summary:
Business Impact:

Finally provide

Key Trends

Articles:

{articles}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt
    )

    newsletter = response.text

    os.makedirs("output", exist_ok=True)

    with open(
        "output/newsletter.md",
        "w",
        encoding="utf-8"
    ) as f:
        f.write(newsletter)

    print("Newsletter generated successfully.")

    return newsletter


if __name__ == "__main__":
    print(generate_newsletter())