# E-Commerce ETL Pipeline using PySpark

## Project Overview
This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline built using PySpark.

## Steps Performed

### 1. Extract
Created structured sample e-commerce sales dataset.

### 2. Transform
- Added revenue column (price × quantity)
- Aggregated total revenue by category

### 3. Load
Exported aggregated results to CSV format.

## Technologies Used
- Python 3
- PySpark
- Java 17
- Homebrew (Mac setup)

## Output
Category-wise total revenue:
- Electronics: 4700
- Clothing: 820

## How to Run
```bash
python3 etl_pipeline.py