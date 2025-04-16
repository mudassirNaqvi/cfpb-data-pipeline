# cfpb-data-pipeline
ETL pipeline to fetch and store CFPB consumer complaints

# CFPB Consumer Complaints Data Pipeline

This project is an automated ETL pipeline designed to fetch, process, and store consumer complaint data from the Consumer Financial Protection Bureau (CFPB) API. The goal is to provide clean, up-to-date data for internal dashboards and monitoring purposes.

## Overview

- Fetches complaint data for **all U.S. states** from the CFPB public API
- Automates data processing using **Apache Airflow**
- Stores cleaned data into:
  - A **Google Sheet** for lightweight reporting
  - A **MySQL database** for structured querying and analytics

## Tech Stack

- **Python** (Pandas, Requests, JSON)
- **Apache Airflow** for orchestration
- **Google Sheets API**
- **MySQL** for data storage

## Architecture

```
CFPB API → Python ETL Scripts → Airflow DAG →
→ Cleaned Data → Google Sheets + MySQL DB
```

## How It Works

1. **Extraction**: Data is pulled from the CFPB API using `requests`, looping through all U.S. states and filtering by date.
2. **Transformation**: Data is cleaned using Pandas—handling missing values, selecting key fields, formatting types.
3. **Loading**: Final data is pushed to:
   - A **Google Sheet** via the `gspread` API
   - A **MySQL database** into a table named `Consumer_Complaints`
4. **Automation**: An **Airflow DAG** orchestrates the entire ETL process on a daily schedule with retry logic and logging.

## Setup Instructions

1. **Clone the repo**:
   ```bash
   git clone https://github.com/mudassirNaqvi/cfpb-data-pipeline.git
   cd cfpb-data-pipeline
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your credentials**:
   - Add your **Google API credentials** for Sheets
   - Set up your **MySQL connection string**

4. **Run via Airflow**:
   ```bash
   airflow scheduler
   airflow webserver
   ```
   Trigger the DAG manually or wait for the scheduled interval.

## Sample Output

- Google Sheet with updated complaint data
- MySQL table `Consumer_Complaints` with structured records

## About Me

**Syed Muhammad Mudassir Naqvi**  
Aspiring Data Engineer passionate about building clean, automated data pipelines and scalable infrastructure.  
📫 [LinkedIn](https://www.linkedin.com/in/syedmuhammadmudassir/) | [GitHub](https://github.com/mudassirNaqvi)

## Notes

- This project was completed as part of a professional assignment simulating real-world data engineering use cases.
- For security, API credentials and environment variables are excluded from the repo.

## License

This project is open-source and available under the MIT License.
