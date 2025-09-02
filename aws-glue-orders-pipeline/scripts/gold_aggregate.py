import sys
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, sum as _sum

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Read from Silver Layer
df = spark.read.parquet("s3://my-dbx-orders-bucket/silver/orders_silver/")

# Aggregate daily sales
df_gold = df.groupBy("order_date").agg(
    _sum(col("amount")).alias("total_sales")
)

# Save to Gold Layer
df_gold.write.mode("overwrite").parquet("s3://my-dbx-orders-bucket/gold/daily_sales/")

job.commit()
