# Databricks ETL Pipeline using PySpark

## Project Overview
This project demonstrates a simple ETL (Extract, Transform, Load) pipeline using PySpark.

## ETL Steps

### 1. Extract
Sample e-commerce order data is created using Spark DataFrame.

### 2. Transform
Data is grouped by product category and total revenue is calculated.

### 3. Load
Aggregated results are exported to CSV format.

## Sample Output
Category-wise total revenue:
- Electronics: 4700
- Clothing: 820

## How to Run

```bash
python3 etl_pipeline.py