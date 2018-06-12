
from pyspark.sql import SparkSession
from pyspark import SparkConf, SparkContext

# Initiate SparkSession
conf = (SparkConf()
         .setMaster("local")
         .setAppName("My app")
         .set("spark.executor.memory", "1g"))
sc = SparkContext(conf = conf)

sc.addPyFile("/opt/spark/dist/sparkling-water-2.2.16.zip")
h2o = __import__("sparkling-water-2.2.16.zip")

# Initiate H2OContext
hc = H2OContext.getOrCreate(spark)

# Stop H2O and Spark services
h2o.cluster().shutdown()
spark.stop()
