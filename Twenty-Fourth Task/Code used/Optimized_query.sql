salesDF = spark.read.parquet("s3://data/sales")
customersDF = spark.read.parquet("s3://data/customers")

usCustomers = customersDF.filter(col("country") == "US")
result = (
    salesDF
    .join(broadcast(usCustomers), on="customerId", how="inner")
    .groupBy("customerId", "customerName")
    .agg(sum("amount").alias("total_sales"))
)
