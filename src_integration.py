"""
src/integration.py

Temporal and spatial aggregation utilities to integrate rainfall and crop production.
"""
import pandas as pd
from typing import Tuple

def aggregate_annual_rainfall(rainfall_df: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregate monthly rainfall to annual totals per state/year.
    Input: rainfall_df with columns ['state','year','month','rainfall_mm']
    Returns: DataFrame with ['state','year','annual_rainfall_mm']
    """
    df = rainfall_df.copy()
    grouped = df.groupby(["state","year"], as_index=False)["rainfall_mm"].sum()
    grouped = grouped.rename(columns={"rainfall_mm":"annual_rainfall_mm"})
    return grouped

def top_crops_by_state_year(crop_df: pd.DataFrame, state: str, year: int, top_n: int = 5) -> pd.DataFrame:
    """
    Return top N crops by production for a state and year.
    """
    df = crop_df.copy()
    filt = df[(df["state"].str.lower() == state.lower()) & (df["year"] == year)]
    grouped = filt.groupby("crop", as_index=False)["production_tonnes"].sum()
    grouped = grouped.sort_values("production_tonnes", ascending=False).head(top_n)
    return grouped

def integrate_crop_and_rainfall(crop_df: pd.DataFrame, rainfall_annual_df: pd.DataFrame) -> pd.DataFrame:
    """
    Merge crop data and annual rainfall by state and year.
    Returns merged DataFrame with columns: state, year, production_tonnes (sum), annual_rainfall_mm
    """
    crop_sum = crop_df.groupby(["state","year"], as_index=False)["production_tonnes"].sum()
    merged = pd.merge(crop_sum, rainfall_annual_df, how="left", on=["state","year"])
    return merged