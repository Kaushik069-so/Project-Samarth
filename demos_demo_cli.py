#!/usr/bin/env python3
"""
demos/demo_cli.py

Simple CLI demo that loads sample CSVs in data/ and answers a question using
the basic Q&A pipeline.
"""
import argparse
import os
import pandas as pd
from src.data_mapper import canonicalize_crop_df, canonicalize_rainfall_df
from src.qa_engine import answer

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")

def load_sample_data():
    crop_path = os.path.join(DATA_DIR, "sample_crop_production.csv")
    rain_path = os.path.join(DATA_DIR, "sample_rainfall.csv")
    if not os.path.exists(crop_path) or not os.path.exists(rain_path):
        print("Sample data not found in data/. Please add CSVs or update docs/data_sources.md with real dataset URLs.")
        return None, None
    crop_df = pd.read_csv(crop_path)
    rain_df = pd.read_csv(rain_path)
    crop_df = canonicalize_crop_df(crop_df)
    rain_df = canonicalize_rainfall_df(rain_df)
    return crop_df, rain_df

def main():
    parser = argparse.ArgumentParser(description="Project Samarth CLI demo")
    parser.add_argument("--question", required=True, help="Natural language question to answer")
    args = parser.parse_args()

    crop_df, rain_df = load_sample_data()
    if crop_df is None:
        return
    result = answer(args.question, crop_df, rain_df)
    # Pretty-print basic result
    import json, textwrap
    print(json.dumps(result, indent=2, default=str))

if __name__ == "__main__":
    main()