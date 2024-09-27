# Databricks notebook source
# MAGIC %run ./_common

# COMMAND ----------

@DBAcademyHelper.monkey_patch
def create_table(self, table_name, location):
    import time
    start = int(time.time())
    
    print(f"Creating the table \"{table_name}\"", end="...")
    spark.sql(f"CREATE OR REPLACE TABLE {table_name} SHALLOW CLONE delta.`{DA.paths.datasets}/{location}`")
        
    print(f"({int(time.time())-start} seconds)")

# COMMAND ----------


