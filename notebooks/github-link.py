# Databricks notebook source
filePath = "dbfs:/databricks-datasets/SPARK_README.md" # path in Databricks File System
lines = sc.textFile(filePath) # read the file into the cluster
lines.take(10) # display first 10 lines in the file