# 🌾 Project Samarth — Intelligent Q&A over Indian Agricultural & Climate Data

## Project Overview
Project Samarth demonstrates the integration of government datasets to answer complex natural-language questions about **India's agriculture** and **climate patterns**. It programmatically discovers datasets from [data.gov.in](https://data.gov.in), performs canonicalization and integration, and provides a prototype Q&A engine that produces **traceable answers with citations**.

---

## Vision & Mission
**Vision:** Enable cross-domain analysis across heterogeneous government datasets for actionable insights.  
**Mission:** Build an intelligent prototype that sources live data, answers questions accurately, and cites datasets for every claim.

---

## Sample Questions
- Compare the average annual rainfall in State_X and State_Y for the last N years and list the top M most produced crops.  
- Identify the highest and lowest producing districts for Crop_Z between two states.  
- Analyze production trends of Crop_Type_C over a decade and correlate with climate data.  
- Provide data-backed recommendations for crop policy decisions.

---

## Repository Structure
Project-Samarth/
Project-Samarth/
├── src/
├── notebooks/
├── demos/
├── data/
├── docs/
├── requirements.txt
├── LICENSE
└── README.md

---

## Setup Instructions
```bash
git clone https://github.com/<username>/Project-Samarth.git
cd Project-Samarth
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
Data Sources & Schema

Crop Production Dataset: state | district | crop | year | production (tonnes)
Rainfall Dataset: state | year | month | rainfall (mm) | latitude/longitude (optional)
(Full resource IDs and URLs are documented in docs/data_sources.md)

python demos/demo_cli.py --question "Compare the average annual rainfall in Maharashtra and Karnataka for the last 5 years and list top 3 most produced cereals"

ANSWER:
Maharashtra rainfall: 1200 mm
Karnataka rainfall: 950 mm
Top 3 crops Maharashtra: Rice, Wheat, Cotton
Top 3 crops Karnataka: Maize, Rice, Sugarcane

CITATIONS:
- IMD Rainfall (https://data.gov.in/resource/xxx)
- Ministry of Agriculture Crop Production (https://data.gov.in/resource/yyy)

Architecture & Design

Flow: Discovery → Canonicalization → Integration → Q&A → Provenance
Highlights:

Datasets programmatically discovered (src/data_gov.py)
Column & unit normalization (src/data_mapper.py)
Temporal & spatial alignment (src/integration.py)
Q&A engine parses questions and synthesizes answers with citations (src/qa_engine.py)
Provenance ensures each numeric result links to dataset, resource ID, and query used
Local execution ensures data sovereignty and privacy

Future Enhancements

Semantic search & vector-based retrieval
ML-based crop prediction and rainfall correlation
Interactive dashboards and visualization notebooks
Automated dataset updates from data.gov.in

