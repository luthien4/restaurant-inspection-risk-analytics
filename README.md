# Restaurant Inspection Risk & Compliance Analytics

Beginner data-engineering and SQL analytics project using official City of Chicago food inspection data.

The goal is to build a small, explainable pipeline from an API response to a SQLite database, then use SQL to answer practical inspection-risk questions.

## Business Question

How can recent food inspection records be used to identify patterns in inspection outcomes, facility-type failure rates, and violation presence?

This first version focuses on a 1,000-row API sample so the full workflow remains easy to inspect, rerun, and explain.

## Data Source

- Source: [City of Chicago Food Inspections](https://data.cityofchicago.org/Health-Human-Services/Food-Inspections/4ijn-s7e5)
- Publisher: City of Chicago
- Format used in this project: Socrata API JSON response
- Sample used: 1,000 most recent inspection records, ordered by inspection date

## Pipeline

![Data engineering pipeline](images/data-engineering-pipeline.svg)

```text
API
-> raw JSON
-> selected fields
-> cleaned JSON
-> cleaned CSV
-> SQLite table
-> verification queries
-> SQL analysis
-> exported analysis CSVs
```

## What This Project Demonstrates

- Requesting JSON data from a public API
- Saving raw API responses locally
- Selecting relevant fields from nested records
- Converting cleaned JSON records into CSV
- Creating a SQLite database table from Python
- Loading CSV records into SQLite
- Verifying the database load with SQL checks
- Writing SQL analysis queries with grouping, conditional counts, percentages, and time-based summaries
- Exporting SQL results as reusable CSV files for future charts

## Repository Structure

```text
.
|-- data/
|   |-- raw/             # ignored raw API/data files
|   `-- processed/       # ignored generated cleaned/export files
|-- database/            # ignored SQLite database files
|-- reports/             # written findings and summaries
|-- scripts/             # Python pipeline and analysis scripts
|-- images/              # future README visuals
|-- README.md
`-- requirements.txt
```

## Main Scripts

| Script | Purpose |
|---|---|
| `01_fetch_api_sample.py` | Fetch 10 API records and inspect the JSON structure |
| `02_select_fields.py` | Keep relevant fields from the 10-row sample |
| `03_clean_json_to_csv.py` | Convert cleaned JSON to CSV |
| `04_fetch_api_sample_1000.py` | Fetch the 1,000 most recent API records |
| `05_clean_api_sample_1000.py` | Save cleaned 1,000-row JSON and CSV files |
| `06_create_sqlite_table.py` | Create the SQLite `inspections` table |
| `07_load_csv_to_sqlite.py` | Load cleaned CSV records into SQLite |
| `08_verify_sqlite_load.py` | Check row counts and result categories |
| `09_analyze_results_distribution.py` | Calculate inspection result distribution |
| `10_failure_rate_by_facility_type.py` | Calculate failure rates by facility type |
| `11_violation_presence_by_result.py` | Compare violation text presence by result |
| `12_inspections_over_time.py` | Analyze monthly inspection volume and failure rates |
| `13_export_monthly_inspection_summary.py` | Export monthly summary metrics to CSV |
| `14_export_facility_failure_rates.py` | Export facility-type failure rates to CSV |

## How To Run

Run scripts from the project root:

```powershell
cd D:\git\restaurant-inspection-risk-analytics
python scripts\04_fetch_api_sample_1000.py
python scripts\05_clean_api_sample_1000.py
python scripts\06_create_sqlite_table.py
python scripts\07_load_csv_to_sqlite.py
python scripts\08_verify_sqlite_load.py
```

Then run the analysis scripts:

```powershell
python scripts\09_analyze_results_distribution.py
python scripts\10_failure_rate_by_facility_type.py
python scripts\11_violation_presence_by_result.py
python scripts\12_inspections_over_time.py
python scripts\13_export_monthly_inspection_summary.py
python scripts\14_export_facility_failure_rates.py
```

In PyCharm, set the working directory to:

```text
D:\git\restaurant-inspection-risk-analytics
```

## Current Sample Outputs

The 1,000-row sample currently shows:

- 578 inspections passed
- 171 inspections failed
- 96 inspections passed with conditions
- Restaurants make up most records in the sample
- Long Term Care, Grocery Store, School, and Restaurant appear among facility types with the highest failure rates in the sample
- Failed and conditional-pass inspections almost always include violation text

Generated analysis exports:

```text
data/processed/monthly_inspection_summary.csv
data/processed/facility_failure_rates.csv
```

These files are generated locally and ignored by Git.

## Next Steps

- Add 2-3 visual highlights from the exported CSV files.
- Expand from the 1,000-row sample to a larger API extract.
- Add more robust data cleaning and data-type conversion.
- Later, parse individual violation codes into a separate table.
