# Project Samarth — Intelligent Q&A over Indian Agricultural & Climate Data

Project Samarth integrates government datasets to answer natural-language questions about India's agriculture and climate patterns. The prototype discovers datasets, canonicalizes and integrates them, and provides a Q&A engine that returns traceable answers with citations.

Vision & Mission
- Vision: Enable cross-domain analysis across heterogeneous government datasets for actionable insights.
- Mission: Build an intelligent prototype that sources live data, answers questions accurately, and cites datasets for every claim.

Quick start
```bash
git clone https://github.com/Kaushik069-so/Project-Samarth.git
cd Project-Samarth
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python demos/demo_cli.py --question "Compare the average annual rainfall in Maharashtra and Karnataka for the last 5 years and list top 3 most produced cereals"
```

Repository layout
```
Project-Samarth/
├── src/
│   ├── data_gov.py
│   ├── data_mapper.py
│   ├── integration.py
│   └── qa_engine.py
├── notebooks/
├── demos/
│   └── demo_cli.py
├── data/
│   ├── sample_crop_production.csv
│   └── sample_rainfall.csv
├── docs/
│   └── data_sources.md
├── requirements.txt
├── LICENSE
└── README.md
```

What this initial code does
- Provides utilities to download resources (stubs), canonicalize columns, integrate crop production and rainfall, and run a simple rule-based Q&A over integrated tables.
- Produces answers with simple provenance (resource placeholders in docs/data_sources.md). Extend file docs/data_sources.md with real resource IDs/URLs for production usage.

Future enhancements
- Robust dataset discovery & automatic update from data.gov.in (API key support).
- Semantic search, vector-based retrieval for provenance.
- Better natural language parsing and uncertainty detection.
- Visualizations and dashboards.
