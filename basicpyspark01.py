from pyspark.sql import SparkSession

# Initialize your SparkSession
spark = SparkSession.builder.appName("CreateDF").getOrCreate()

# 1. Define your data as a list of lists (or list of tuples)
data = [
    ["Alice", 25],
    ["Bob", 30],
    ["Charlie", 35]
]

# 2. Define your column names
columns = ["Name", "Age"]

# 3. Create the DataFrame
df = spark.createDataFrame(data, schema=columns)

# Display the results
df.show()
