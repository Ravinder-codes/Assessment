# Assessment

## Overview
This project is focused on **cleaning and filtering customer, product, and order data** to extract meaningful insights. It provides scripts to process raw datasets and generate cleaned outputs ready for analysis.

## Repository Structure
```
Assessment/ 
│
├── raw_data/          # Original datasets (customers, orders, products)
├── cleaned_data/      # Output of cleaned CSV files
├── utils/             # Utility scripts for data processing
├── clean_data.py      # Script to clean raw data
├── analyze.py         # Script to analyze cleaned data (upcoming)
├── constants.py       # Project constants
└── README.md          # Project documentation
```
## Getting Started

1. **Clone the repository**
git clone https://github.com/Ravinder-codes/Assessment.git
cd Assessment

2. **Install required libraries**
```
-pandas
-logger
```
3. **Run data cleaning**
python clean_data.py
This script reads files from `raw_data/` and outputs cleaned CSVs in `cleaned_data/`.

4. **Analyze cleaned data**
python analyze.py
This will generate insights and summaries from the cleaned data into analysis data.

## Features
- Cleans raw datasets with inconsistent formats and missing values.
- Standardizes dates, emails, and other fields.
- Prepares data for analysis and reporting.
- Automated insights.
