from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.types import IntegerType

spark = SparkSession.builder.appName("Data8277Processing").getOrCreate()

input_path = "s3://aws-emr-large-data/Data8277.csv"
output_path = "s3://aws-emr-large-data/output/area_count_summary.csv"

df = spark.read.option("header", "true").csv(input_path)

df = df.withColumn("Year", col("Year").cast(IntegerType())) \
       .withColumn("Age", col("Age").cast(IntegerType())) \
       .withColumn("Ethnic", col("Ethnic").cast(IntegerType())) \
       .withColumn("Sex", col("Sex").cast(IntegerType())) \
       .withColumn("Area", col("Area").cast(IntegerType())) \
       .withColumn("count", col("count").cast(IntegerType()))

df_clean = df.dropna(subset=["Area", "count"])

result = df_clean.groupBy("Area").sum("count").withColumnRenamed("sum(count)", "total_count")

result.write.mode("overwrite").option("header", "true").csv(output_path)

spark.stop()
