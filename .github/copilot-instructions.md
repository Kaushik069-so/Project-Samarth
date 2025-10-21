# Copilot Instructions for Project Samarth

## Project Overview

Project Samarth is an intelligent Q&A system that integrates Indian agricultural and climate datasets from data.gov.in. The system enables natural language queries over government datasets to answer complex questions about India's agriculture and climate patterns with traceable citations.

**Vision:** Enable cross-domain analysis across heterogeneous government datasets for actionable insights.
**Mission:** Build an intelligent prototype that sources live data, answers questions accurately, and cites datasets for every claim.

## Repository Structure

```
Project-Samarth/
├── src/              # Core source code
├── notebooks/        # Jupyter notebooks for analysis
├── demos/           # Demo applications and CLI tools
├── data/            # Data files and schemas
├── docs/            # Documentation
├── requirements.txt # Python dependencies
├── LICENSE
└── README.md
```

## Key Components

### Data Pipeline
- **src/data_gov.py**: Programmatically discovers datasets from data.gov.in
- **src/data_mapper.py**: Handles column and unit normalization
- **src/integration.py**: Performs temporal and spatial alignment
- **src/qa_engine.py**: Parses questions and synthesizes answers with citations

### Data Schema
- **Crop Production Dataset**: state | district | crop | year | production (tonnes)
- **Rainfall Dataset**: state | year | month | rainfall (mm) | latitude/longitude (optional)

## Development Guidelines

### Python Environment Setup
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Coding Standards
- Follow PEP 8 style guidelines for Python code
- Use type hints where applicable
- Write docstrings for all functions and classes
- Keep functions focused and modular

### Data Handling
- Always validate data from data.gov.in before processing
- Implement proper error handling for API calls
- Cache datasets appropriately to minimize API calls
- Ensure data sovereignty and privacy by processing locally

### Provenance & Citations
- Every data point must be traceable to its source
- Include resource IDs and URLs in all responses
- Maintain dataset metadata throughout the pipeline
- Link numeric results to the dataset and query used

### Testing
- Write unit tests for data processing functions
- Validate Q&A outputs against expected results
- Test edge cases for dataset integration
- Verify citation accuracy

### Documentation
- Update docs/data_sources.md when adding new datasets
- Document API changes in relevant module docstrings
- Keep README.md examples current and working
- Add inline comments for complex data transformations

## Common Tasks

### Adding a New Dataset
1. Update src/data_gov.py with discovery logic
2. Define schema mapping in src/data_mapper.py
3. Add integration rules to src/integration.py
4. Document in docs/data_sources.md
5. Add example queries to README.md

### Extending the Q&A Engine
1. Identify the question pattern
2. Implement parsing logic in src/qa_engine.py
3. Add citation tracking
4. Test with real datasets
5. Add examples to documentation

### Running Demos
```bash
python demos/demo_cli.py --question "Your question here"
```

## Best Practices

- **Data Quality**: Always validate and clean data before analysis
- **Performance**: Use efficient data structures (pandas DataFrames, numpy arrays)
- **Scalability**: Design for incremental dataset updates
- **Error Handling**: Provide informative error messages
- **Citations**: Never present data without proper attribution
- **Local Processing**: Maintain data sovereignty by processing locally

## Future Enhancement Areas
- Semantic search & vector-based retrieval
- ML-based crop prediction and rainfall correlation
- Interactive dashboards and visualization
- Automated dataset updates from data.gov.in

## Important Notes

- This project focuses on Indian government data sources
- Data accuracy and proper citation are paramount
- All answers must be traceable to source datasets
- Privacy and data sovereignty must be maintained
