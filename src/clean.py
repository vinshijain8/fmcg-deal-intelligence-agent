"""
clean.py

Purpose:
---------
Clean the raw news data.

Input:
    data/raw_news.csv

Output:
    data/cleaned_news.csv
"""

import os
import pandas as pd


def clean_news():
    # -----------------------------
    # File paths
    # -----------------------------
    INPUT_FILE = "data/raw_news.csv"
    OUTPUT_FILE = "data/cleaned_news.csv"

    print("=" * 60)
    print("Cleaning News Data")
    print("=" * 60)

    # -----------------------------
    # Read CSV
    # -----------------------------
    df = pd.read_csv(INPUT_FILE)

    print(f"\nOriginal articles : {len(df)}")

    # -----------------------------
    # Remove rows with missing title
    # -----------------------------
    df.dropna(subset=["Title"], inplace=True)

    # -----------------------------
    # Remove rows with missing description
    # -----------------------------
    df.dropna(subset=["Description"], inplace=True)

    # -----------------------------
    # Remove duplicate URLs
    # -----------------------------
    df.drop_duplicates(subset="URL", inplace=True)

    # -----------------------------
    # Remove extra spaces
    # -----------------------------
    df["Title"] = df["Title"].str.strip()
    df["Description"] = df["Description"].str.strip()
    df["Source"] = df["Source"].str.strip()

    # -----------------------------
    # Reset Index
    # -----------------------------
    df.reset_index(drop=True, inplace=True)

    # -----------------------------
    # Save cleaned file
    # -----------------------------
    os.makedirs("data", exist_ok=True)

    df.to_csv(OUTPUT_FILE, index=False)

    print(f"Articles after cleaning : {len(df)}")

    print(f"\nSaved to {OUTPUT_FILE}")

    print("\nPreview\n")
    print(df.head())

    return df


if __name__ == "__main__":
    clean_news()