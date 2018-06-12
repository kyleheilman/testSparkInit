from pysparkling import *
from pyspark.sql import SparkSession


# Initiate SparkSession
spark = SparkSession.builder.appName("App name").getOrCreate()
spark.addPyFile("sparkling-water-2.2.16.zip")
import sparkling-water-2.2.16.zip as h2o

# Initiate H2OContext
hc = H2OContext.getOrCreate(spark)

# Stop H2O and Spark services
h2o.cluster().shutdown()
spark.stop()