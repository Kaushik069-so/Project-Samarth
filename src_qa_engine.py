"""
src/qa_engine.py

A simple rule-based Q&A engine that can answer a few types of questions using
the integrated dataframes. For complex questions, replace with an NLP parser or LLM pipeline.
"""
import re
from typing import Tuple, List, Dict, Any
import pandas as pd
from .integration import aggregate_annual_rainfall, top_crops_by_state_year, integrate_crop_and_rainfall

# Basic provenance info (map dataset keys to docs entries)
PROVENANCE = {
    "rainfall": {
        "name": "IMD Rainfall (placeholder)",
        "url": "<docs/data_sources.md#rainfall-dataset>"
    },
    "crop": {
        "name": "Ministry of Agriculture - Crop Production (placeholder)",
        "url": "<docs/data_sources.md#crop-production-dataset>"
    }
}

def parse_compare_rainfall_question(q: str) -> Tuple[List[str], int, int]:
    """
    Parse questions like:
    "Compare the average annual rainfall in Maharashtra and Karnataka for the last 5 years and list top 3 most produced cereals"
    Returns: ([state1, state2, ...], last_n_years, top_m)
    """
    states = re.findall(r"in\s+([A-Za-z,\s]+?)\s+for", q)
    if states:
        state_text = states[0]
        state_list = [s.strip() for s in state_text.split("and") if s.strip()]
    else:
        # fallback: find capitalized words near 'and'
        state_list = re.findall(r"\b([A-Z][a-z]+)\b", q)
    years_n = 5
    m_top = 3
    m_match = re.search(r"top\s+(\d+)", q)
    if m_match:
        m_top = int(m_match.group(1))
    years_match = re.search(r"last\s+(\d+)\s+years", q)
    if years_match:
        years_n = int(years_match.group(1))
    return state_list, years_n, m_top

def answer_compare_rainfall_and_top_crops(q: str, crop_df: pd.DataFrame, rainfall_df: pd.DataFrame) -> Dict[str,Any]:
    states, last_n, top_m = parse_compare_rainfall_question(q)
    # Determine year window from available data
    max_year = max(rainfall_df["year"].max(), crop_df["year"].max())
    min_year = max_year - last_n + 1
    rf_window = rainfall_df[(rainfall_df["year"] >= min_year) & (rainfall_df["year"] <= max_year)]
    rf_annual = aggregate_annual_rainfall(rf_window)
    results = {}
    citations = []
    for s in states:
        s_rf = rf_annual[rf_annual["state"].str.lower() == s.lower()]
        avg = s_rf["annual_rainfall_mm"].mean() if not s_rf.empty else None
        # For crops, get aggregated top crops over the same window: sum production across years then rank
        crops_window = crop_df[(crop_df["state"].str.lower() == s.lower()) & (crop_df["year"] >= min_year) & (crop_df["year"] <= max_year)]
        top_crops = crops_window.groupby("crop", as_index=False)["production_tonnes"].sum().sort_values("production_tonnes", ascending=False).head(top_m)
        results[s] = {
            "avg_annual_rainfall_mm": float(avg) if avg is not None and not pd.isna(avg) else None,
            "top_crops": top_crops.to_dict(orient="records")
        }
    citations.append(PROVENANCE["rainfall"])
    citations.append(PROVENANCE["crop"])
    return {"question": q, "years": (min_year, max_year), "results": results, "citations": citations}

def answer(q: str, crop_df: pd.DataFrame, rainfall_df: pd.DataFrame) -> Dict[str,Any]:
    q_lower = q.lower()
    if "compare" in q_lower and "rainfall" in q_lower:
        return answer_compare_rainfall_and_top_crops(q, crop_df, rainfall_df)
    else:
        return {"question": q, "error": "Question type not supported by the simple engine yet."}