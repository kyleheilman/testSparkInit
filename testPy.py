from pyspark.sql import SparkSession
from pyspark import SparkConf, SparkContext

# Initiate SparkSession
spark = SparkSession\
    .builder\
    .appName("PythonPi")\
    .getOrCreate()

spark.sparkContext.addPyFile("/mnt/mesos/sandbox/sparkling-water-2.2.16.zip")
h2o = __import__("sparkling-water-2.2.16")

# Initiate H2OContext
hc = H2OContext.getOrCreate(spark)

# Stop H2O and Spark services
h2o.cluster().shutdown()
spark.stop()
