#!/usr/bin/env python3

from pyspark.sql import SparkSession as SP
import pandas as pd


def main():
    # Initialize SparkSession from 
    spark = SP.builder \
        .appName("Read Excel with PySpark") \
        .getOrCreate()

    # Read Excel file into pandas DataFrame
    file_path = "lab-reports.xlsx"
    df = pd.read_excel(file_path)

    # Convert pandas DataFrame to Spark DataFrame
    spark_df = spark.createDataFrame(df)

    # Display contents of Spark DataFrame
    print("Contents of lab-reports.xlsx:")
    spark_df.show()

    # Stop SparkSession
    spark.stop()


if __name__ == '__main__':
    main() 
    
# this code was interpreted on a linux machine becuase spark was not installing correctly in windows