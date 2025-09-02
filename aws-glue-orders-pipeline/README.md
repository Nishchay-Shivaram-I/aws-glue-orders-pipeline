# AWS Glue Data Lake Pipeline – Orders Analytics

This project builds a real-time data pipeline using AWS Glue, S3, and PySpark. It follows the Bronze–Silver–Gold architecture pattern to ingest, clean, and aggregate order data from CSV to analytics-ready formats.

## 🛠️ Tools Used
- AWS S3
- AWS Glue Studio (Spark)
- PySpark (via Glue)
- IAM roles
- Python 3

## 🧱 Pipeline Architecture

Raw CSV (S3: /raw/orders.csv)
↓ [bronze_ingest.py]
Bronze Layer (Parquet: /bronze/orders_bronze/)
↓ [silver_clean.py]
Silver Layer (Typed: /silver/orders_silver/)
↓ [gold_aggregate.py]
Gold Layer (Aggregated: /gold/daily_sales/)


## 📂 Folder Structure

aws-glue-orders-pipeline/
├── README.md
├── scripts/
│ ├── bronze_ingest.py
│ ├── silver_clean.py
│ └── gold_aggregate.py


## 🔍 Description of ETL Jobs

### 1. `bronze_ingest.py`
Ingests raw `orders.csv` from S3 and stores it as Parquet in the Bronze layer.

### 2. `silver_clean.py`
Cleans and typecasts the Bronze data into structured columns like `order_id`, `amount`, and `order_date`.

### 3. `gold_aggregate.py`
Aggregates daily sales totals and writes results to the Gold layer.

## ✅ Output Example

| order_date | total_sales |
|------------|-------------|
| 2023-08-01 | 220.49      |
| 2023-08-02 | 350.00      |
| 2023-08-03 | 80.00       |

## 💡 Future Improvements

- Query with Athena
- Visualize in QuickSight
- Add data quality checks
- Schedule with Glue Workflows

---

## 👤 Author

**Nishchay S**  
[GitHub Profile](https://github.com/Nishchay-Shivaram-I)

---

## 📜 License

MIT – do whatever you want 😎

