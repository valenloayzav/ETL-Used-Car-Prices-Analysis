# ETL Used Car Prices Analysis

This project is part of the IBM Data Analyst Professional Certificate (Coursera). It demonstrates an ETL (Extract, Transform, Load) process using Python for data extraction from multiple formats (CSV, JSON, XML), transformation of values, and loading into a final consolidated CSV file.

## Technologies Used
- Python
- Pandas
- xml.etree.ElementTree
- datetime
- glob
- Cloud IDE

## Project Structure
- **etl_practice.py**: Main script that runs the ETL pipeline.
- **data/**: Contains all raw data files in CSV, JSON, and XML format.
- **transformed_data.csv**: Output file with rounded prices.
- **log_file.txt**: Logs of all steps in the ETL pipeline.

## Process Overview
### 1. Extract
Data is extracted from three files of each format: `.csv`, `.json`, `.xml`, containing:
- `car_model`
- `year_of_manufacture`
- `price`
- `fuel`
### 2. Transform
The 'price' column is converted to float and rounded to two decimal places.
### 3. Load
The transformed data is saved into `transformed_data.csv`.

## How to Run
1. Clone the repository.
2. Install dependencies (terminal): pip install -r requirements.txt
3. Run the pipeline (terminal): python3.11 etl_practice.py

## Outcome
A single, cleaned dataset ready for analysis.

## Learning Objective
This exercise is part of Coursera's **"Python for Data Science, AI & Development"** course and aims to demonstrate practical skills in ETL using Python and pandas.

---
