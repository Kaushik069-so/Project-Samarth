# Project Samarth — Intelligent Q&A over Indian Agricultural & Climate Data

Project Samarth is a prototype system that integrates heterogeneous government datasets to answer natural-language questions about India's agriculture and climate patterns. The system demonstrates data discovery, canonicalization, integration, and a Q&A engine capable of producing traceable answers with citations.

---

## Vision & Mission
- **Vision:** Enable cross-domain analysis across government datasets for actionable insights.
- **Mission:** Build an intelligent prototype that sources live datasets, accurately answers natural-language queries, and cites every data source used.

---

## Sample Questions
- Compare the average annual rainfall in State_X and State_Y for the last N years and list the top M most produced crops.
- Identify the district with the highest and lowest production of a crop in two states.
- Analyze crop production trends over the last decade and correlate with climate data.
- Provide data-backed recommendations for crop policy or planning decisions.

---

## Quick Start

```bash
git clone https://github.com/Kaushik069-so/Project-Samarth.git
cd Project-Samarth

# Create virtual environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# Install required packages
pip install -r requirements.txt

# Run CLI demo
python demos/demo_cli.py --question "Compare the average annual rainfall in Maharashtra and Karnataka for the last 5 years and list top 3 most produced cereals"

What this initial code does
- Provides utilities to download resources (stubs), canonicalize columns, integrate crop production and rainfall, and run a simple rule-based Q&A over integrated tables.
- Produces answers with simple provenance (resource placeholders in docs/data_sources.md). Extend file docs/data_sources.md with real resource IDs/URLs for production usage.

Project-Samarth/
├── src/                   # Core Python modules
│   ├── data_gov.py        # Dataset discovery/download utilities
│   ├── data_mapper.py     # Canonicalize column names and units
│   ├── integration.py     # Merge crop & rainfall data
│   └── qa_engine.py       # Question parsing & answer synthesis
├── notebooks/             # Interactive demos
│   ├── 01_data_discovery.ipynb
│   ├── 02_integration_demo.ipynb
│   └── 03_qa_demo.ipynb
├── demos/                 # CLI demo
│   └── demo_cli.py
├── data/                  # Sample datasets
│   ├── sample_crop_production.csv
│   └── sample_rainfall.csv
├── docs/                  # Documentation
│   └── data_sources.md
├── requirements.txt       # Python dependencies
├── LICENSE                # MIT License
└── README.md

What This Code Does:
Provides utilities to download resources (stubs), canonicalize columns, integrate crop production and rainfall, and run a simple rule-based Q&A over integrated tables.
Produces answers with simple provenance (resource placeholders in docs/data_sources.md). Extend docs/data_sources.md with real resource IDs/URLs for production use.

Example CLI Usage:
python demos/demo_cli.py --question "Compare the average annual rainfall in Maharashtra and Karnataka for the last 5 years and list top 3 most produced cereals"

Sample Output:
Question: Compare the average annual rainfall in Maharashtra and Karnataka for the last 5 years and list top 3 most produced cereals

Answer:
Maharashtra rainfall: 1200 mm
Karnataka rainfall: 950 mm
Top 3 crops Maharashtra: Rice, Wheat, Cotton
Top 3 crops Karnataka: Maize, Rice, Sugarcane

Citations:
- IMD Rainfall (https://data.gov.in/resource/yyy)
- Ministry of Agriculture Crop Production (https://data.gov.in/resource/xxx)

Future Enhancements:
Robust dataset discovery & automatic updates from data.gov.in (API key support).
Semantic search and vector-based retrieval for improved provenance.
Advanced natural-language parsing and uncertainty detection.
Interactive visualizations and dashboards.
Policy analysis tools, recommendations, and alerts based on integrated historical data.

