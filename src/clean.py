import os
import pandas as pd


def clean_news():
   
    INPUT_FILE = "data/raw_news.csv"
    OUTPUT_FILE = "data/cleaned_news.csv"

    print("=" * 60)
    print("Cleaning News Data")
    print("=" * 60)


    df = pd.read_csv(INPUT_FILE)

    print(f"\nOriginal articles : {len(df)}")

    df.dropna(subset=["Title"], inplace=True)


    df.dropna(subset=["Description"], inplace=True)

    df.drop_duplicates(subset="URL", inplace=True)


    df["Title"] = df["Title"].str.strip()
    df["Description"] = df["Description"].str.strip()
    df["Source"] = df["Source"].str.strip()


    df.reset_index(drop=True, inplace=True)

    os.makedirs("data", exist_ok=True)

    df.to_csv(OUTPUT_FILE, index=False)

    print(f"Articles after cleaning : {len(df)}")

    print(f"\nSaved to {OUTPUT_FILE}")

    print("\nPreview\n")
    print(df.head())

    return df


if __name__ == "__main__":
    clean_news()