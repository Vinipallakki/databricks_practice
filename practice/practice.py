# Databricks notebook source
from pyspark.sql import SparkSession
from pyspark.sql.types import StringType, StructField, StringType, IntegerType, StructType
spark = SparkSession.builder \
        .appName("myapp")   \
        .getOrCreate()


# COMMAND ----------

print(spark.version)

# COMMAND ----------

data = [("Alice", 34), ("Bob", 45), ("Cathy", 29)]
schema = StructType([
    StructField("Name", StringType(), True),
    StructField("Age", IntegerType(), True)
])

df = spark.createDataFrame(data, schema)
df.show()

# COMMAND ----------

#i have added some extra data from this
from pyspark.sql import Row

# Generate additional 50 rows of data
additional_data = [("Person" + str(i), 20 + i % 30) for i in range(50)]

# Convert the additional data to a DataFrame
additional_df = spark.createDataFrame(additional_data, schema)

# Union the original DataFrame with the additional DataFrame
df = df.union(additional_df)

display(df)

# COMMAND ----------

from pyspark.sql.functions import col, lit

# Add a new column 'Salary' with some example data
df = df.withColumn("Salary", (col("Age") * 1000) + 30000)
df.printSchema()


# COMMAND ----------



# COMMAND ----------


