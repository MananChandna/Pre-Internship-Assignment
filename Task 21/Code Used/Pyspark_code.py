import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode, split, count
import matplotlib.pyplot as plt

os.environ["JAVA_HOME"] = r"C:\Program Files\Java\jdk-11"
os.environ["SPARK_HOME"] = r"C:\spark"

spark = SparkSession.builder \
    .appName("LargeCSV_EDA_OpenFoodFacts") \
    .master("local[*]") \
    .getOrCreate()

csv_path = r"C:\Users\Manan\Downloads\en.openfoodfacts.org.products.csv"
output_dir = r"C:\Users\Manan\Downloads\openfoodfacts_france_output"

df = spark.read.option("header", True).option("sep", "\t").csv(csv_path)

print("\n=== Data Schema ===")
df.printSchema()

print("\n=== Total Products Count ===")
print(df.count())

df_countries = df.select(explode(split(col("countries"), ",")).alias("country"))
df_country_counts = df_countries.groupBy("country").agg(count("*").alias("product_count"))
df_country_counts_filtered = df_country_counts.filter(col("product_count") >= 5000)

pdf_country_counts = df_country_counts_filtered.toPandas().sort_values(by="product_count", ascending=False)

plt.figure(figsize=(12, 6))
plt.barh(pdf_country_counts["country"], pdf_country_counts["product_count"])
plt.xlabel("Product Count")
plt.title("Countries with ≥ 5000 Products")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

df_france = df.filter(col("countries").like("%France%"))

df_france.write.mode("overwrite").option("header", True).csv(output_dir)

print(f"\nFiltered data for France saved to: {output_dir}")
