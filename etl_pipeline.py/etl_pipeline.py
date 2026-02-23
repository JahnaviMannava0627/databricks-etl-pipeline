from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as _sum

# Create Spark session
spark = SparkSession.builder \
    .appName("Ecommerce_ETL_Pipeline") \
    .getOrCreate()

# ------------------ EXTRACT ------------------

data = [
    (1, "Laptop", "Electronics", 800, 2),
    (2, "Phone", "Electronics", 500, 5),
    (3, "Shirt", "Clothing", 40, 10),
    (4, "Shoes", "Clothing", 60, 7),
    (5, "Headphones", "Electronics", 150, 4)
]

columns = ["order_id", "product", "category", "price", "quantity"]

df = spark.createDataFrame(data, columns)

print("Raw Data:")
df.show()

# ------------------ TRANSFORM ------------------

df_transformed = df.withColumn(
    "revenue",
    col("price") * col("quantity")
)

print("Transformed Data:")
df_transformed.show()

df_aggregated = df_transformed.groupBy("category") \
    .agg(_sum("revenue").alias("total_revenue"))

print("Aggregated Revenue by Category:")
df_aggregated.show()

# ------------------ LOAD ------------------

df_aggregated.write.mode("overwrite").csv("output", header=True)

print("ETL Pipeline Completed Successfully!")

spark.stop()