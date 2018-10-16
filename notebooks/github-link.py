# Databricks notebook source
# MAGIC %md
# MAGIC ##WordCount Example

# COMMAND ----------

# MAGIC %md
# MAGIC #### Step 1: Load text file from our Hosted Datasets. Shift-Enter Runs the code below.

# COMMAND ----------

filePath = "dbfs:/databricks-datasets/SPARK_README.md" # path in Databricks File System
lines = sc.textFile(filePath) # read the file into the cluster
lines.take(10) # display first 10 lines in the file

# COMMAND ----------

# MAGIC %md 
# MAGIC #### Step 2: Inspect the number of partitions (workers) used to store the dataset

# COMMAND ----------

