"""
src/data_mapper.py

Column normalization, data canonicalization and unit conversion helpers.
"""
from typing import Dict
import pandas as pd
import numpy as np

# Standard column names used across the project
CROP_COLUMNS = ["state", "district", "crop", "year", "production_tonnes"]
RAINFALL_COLUMNS = ["state", "year", "month", "rainfall_mm", "latitude", "longitude"]

def canonicalize_crop_df(df: pd.DataFrame, col_map: Dict[str,str] = None) -> pd.DataFrame:
    """
    Rename columns to canonical crop columns and convert production to tonnes where possible.
    col_map: optional mapping from current column names to canonical names.
    """
    df = df.copy()
    if col_map:
        df = df.rename(columns=col_map)
    # Lowercase column names for matching
    df.columns = [c.lower().strip() for c in df.columns]
    # Common fallbacks
    if "production" in df.columns and "production_tonnes" not in df.columns:
        df = df.rename(columns={"production": "production_tonnes"})
    # Ensure year is int
    if "year" in df.columns:
        df["year"] = df["year"].astype(int)
    # If production value appears to be in quintals (>=1000 for many entries), try heuristic conversion
    if "production_tonnes" in df.columns:
        vals = df["production_tonnes"]
        # If median is large but units unclear, we assume it's already in tonnes.
        df["production_tonnes"] = pd.to_numeric(vals, errors="coerce")
    # Return only canonical columns if present
    present = [c for c in CROP_COLUMNS if c in df.columns]
    return df[present]

def canonicalize_rainfall_df(df: pd.DataFrame, col_map: Dict[str,str] = None) -> pd.DataFrame:
    """
    Rename columns to canonical rainfall columns and ensure numeric types.
    """
    df = df.copy()
    if col_map:
        df = df.rename(columns=col_map)
    df.columns = [c.lower().strip() for c in df.columns]
    if "rain" in df.columns and "rainfall_mm" not in df.columns:
        df = df.rename(columns={"rain": "rainfall_mm", "rain_mm": "rainfall_mm"})
    if "year" in df.columns:
        df["year"] = df["year"].astype(int)
    if "month" in df.columns:
        df["month"] = df["month"].astype(int)
    if "rainfall_mm" in df.columns:
        df["rainfall_mm"] = pd.to_numeric(df["rainfall_mm"], errors="coerce").fillna(0.0)
    present = [c for c in RAINFALL_COLUMNS if c in df.columns]
    return df[present]