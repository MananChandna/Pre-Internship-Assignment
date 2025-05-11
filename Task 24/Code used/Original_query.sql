salesDF = spark.read.parquet("s3://data/sales")
customersDF = spark.read.parquet("s3://data/customers")

result = (
    salesDF
    .join(customersDF, on="customerId", how="inner")
    .filter(customersDF.country == "US")
    .groupBy("customerId", "customerName")
    .agg(sum("amount").alias("total_sales"))
)
