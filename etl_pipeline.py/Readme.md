# Databricks ETL Pipeline using PySpark

## 📌 Project Overview
This project demonstrates a simple ETL (Extract, Transform, Load) pipeline built using PySpark.

The pipeline processes sample e-commerce sales data, performs revenue aggregation, and exports the final results into CSV format.

---

## 🛠 Technologies Used
- Python 3
- PySpark
- Git & GitHub
- VS Code
- Homebrew (Mac setup)

---

## 🔄 ETL Steps

### 1️⃣ Extract
Loaded sample e-commerce transaction data into a Spark DataFrame.

### 2️⃣ Transform
- Created a new `revenue` column (price × quantity)
- Aggregated total revenue by product category

### 3️⃣ Load
Exported aggregated results to CSV format.

---

## 📊 Sample Output

Category-wise total revenue:
- Electronics: 4700
- Clothing: 820

---

## ▶️ How to Run

```bash
python3 etl_pipeline.py