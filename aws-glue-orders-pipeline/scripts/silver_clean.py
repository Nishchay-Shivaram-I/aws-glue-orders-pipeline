import sys
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Read from Bronze (Parquet)
df = spark.read.parquet("s3://my-dbx-orders-bucket/bronze/orders_bronze/")

# Apply data types
from pyspark.sql.functions import col, to_date

df_clean = df.select(
    col("order_id").cast("int"),
    col("customer_id"),
    to_date(col("order_date"), "yyyy-MM-dd").alias("order_date"),
    col("amount").cast("double")
)

# Write to Silver Layer
df_clean.write.mode("overwrite").parquet("s3://my-dbx-orders-bucket/silver/orders_silver/")

job.commit()
