# Databricks notebook source
df = spark.table("default.full_property_list_oc")
df.printSchema()
df.show(5)


# COMMAND ----------

# Remove rows where property name starts with (Accounting Only)
df_clean = df.filter(~df["Property"].startswith("(Accounting Only)"))

# Optional: Drop unused or entirely null columns
columns_to_drop = ["Owner Agent", "Online Maintenance Request Instructions", "Amenities"]
df_clean = df_clean.drop(*columns_to_drop)

# Show a preview of the cleaned data
df_clean.show(5)


# COMMAND ----------

delta_path = "dbfs:/FileStore/delta/property_data"
# Clean column names to remove spaces, parentheses, and special characters
from pyspark.sql.functions import col

for old_name in df_clean.columns:
    new_name = old_name.strip().lower().replace(" ", "_").replace("(", "").replace(")", "").replace("-", "_")
    df_clean = df_clean.withColumnRenamed(old_name, new_name)

# Show cleaned column names
print(df_clean.columns)

df_clean.write.format("delta").mode("overwrite").save(delta_path)


# COMMAND ----------

delta_path = "dbfs:/FileStore/delta/property_data"

df_clean.write.format("delta").mode("overwrite").save(delta_path)


# COMMAND ----------

spark.sql("DROP TABLE IF EXISTS default.property_data_delta")
spark.sql("""
  CREATE TABLE default.property_data_delta
  USING DELTA
  LOCATION 'dbfs:/FileStore/delta/property_data'
""")


# COMMAND ----------

spark.sql("SELECT * FROM default.property_data_delta LIMIT 10").show()
