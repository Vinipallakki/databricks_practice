# Databricks notebook source
from pyspark.sql import SparkSession
from pyspark.sql.functions import ceil,sum
spark = SparkSession.builder \
    .appName("nyc_data") \
    .getOrCreate()


# COMMAND ----------


df = spark.read.table("samples.nyctaxi.trips")
df_1 = df.drop("pickup_zip","dropoff_zip")
df_2_ceil = df_1.withColumn("trip_distance",ceil(df_1["trip_distance"]))
df_2_ceil_final = df_2_ceil.withColumn("fare_amount",ceil(df_2_ceil["fare_amount"]))
display(df_2_ceil_final)
df_sum = df_2_ceil_final.agg(sum("trip_distance"))


# COMMAND ----------

df_2_ceil_final.write.csv("/samples.nyctaxi.nyc_data.csv", header=True)


# COMMAND ----------

dbutils.fs.ls("/samples.nyctaxi.nyc_data.csv")

# COMMAND ----------


