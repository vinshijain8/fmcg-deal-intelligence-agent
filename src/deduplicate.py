import os
import pandas as pd
from rapidfuzz import fuzz


def deduplicate_news():

    INPUT_FILE = "data/relevant_news.csv"
    OUTPUT_FILE = "data/deduplicated_news.csv"

    print("=" * 60)
    print("Removing Near-Duplicate Articles")
    print("=" * 60)

    # Read filtered data
    df = pd.read_csv(INPUT_FILE)

    print(f"\nArticles before deduplication: {len(df)}")

    unique_articles = []

    SIMILARITY_THRESHOLD = 90

    for _, row in df.iterrows():

        title = str(row["Title"])

        duplicate = False

        for saved_article in unique_articles:

            similarity = fuzz.ratio(
                title.lower(),
                str(saved_article["Title"]).lower()
            )

            if similarity >= SIMILARITY_THRESHOLD:
                duplicate = True
                break

        if not duplicate:
            unique_articles.append(row)

    # Convert back to DataFrame
    deduplicated_df = pd.DataFrame(unique_articles)

    os.makedirs("data", exist_ok=True)

    deduplicated_df.to_csv(OUTPUT_FILE, index=False)

    print(f"Articles after deduplication: {len(deduplicated_df)}")

    print(f"\nSaved to {OUTPUT_FILE}")

    print("\nPreview\n")
    print(deduplicated_df.head())

    return deduplicated_df


if __name__ == "__main__":
    deduplicate_news()