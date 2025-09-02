import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

# Required job params
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

# Glue and Spark context
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Read CSV from raw folder in S3
df = spark.read.option("header", "true").csv("s3://my-dbx-orders-bucket/raw/orders.csv")

# Write it as Parquet to bronze layer
df.write.mode("overwrite").format("parquet").save("s3://my-dbx-orders-bucket/bronze/orders_bronze/")

job.commit()
