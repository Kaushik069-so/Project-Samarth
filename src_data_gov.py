"""
src/data_gov.py

Simple helpers for fetching dataset files. These are small utilities and
stubs for integrating with data.gov.in APIs. For production, add API-key support
and robust error-handling.
"""
import os
import requests
from typing import Optional

def download_csv(url: str, dest_path: str, chunk_size: int = 1024) -> None:
    """
    Download a CSV from a URL to dest_path. Overwrites if exists.
    """
    os.makedirs(os.path.dirname(dest_path) or ".", exist_ok=True)
    with requests.get(url, stream=True, timeout=30) as r:
        r.raise_for_status()
        with open(dest_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=chunk_size):
                if chunk:
                    f.write(chunk)

def fetch_resource_from_datagov(resource_api_url: str, params: Optional[dict] = None, api_key: Optional[str] = None) -> dict:
    """
    Placeholder for calling data.gov.in resource API endpoints.
    - resource_api_url: full API endpoint for the resource (e.g., data.gov.in)
    - params: API parameters
    - api_key: optional API key
    Returns parsed JSON on success.
    """
    headers = {}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"
    resp = requests.get(resource_api_url, params=params or {}, headers=headers, timeout=30)
    resp.raise_for_status()
    return resp.json()