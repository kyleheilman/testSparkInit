
from pyspark.sql import SparkSession
from pyspark import SparkConf, SparkContext, SparkFiles
import sys

# Initiate SparkSession
spark = SparkSession\
    .builder\
    .appName("PythonPi")\
    .getOrCreate()

spark.sparkContext.addPyFile("/mnt/mesos/sandbox/sparkling-water-2.2.16.zip")

sys.path.insert(0, '/mnt/mesos/sandbox/sparkling-water-2.2.16/py/build/dist/h2o_pysparkling_2.2-2.2.16.zip')
print(SparkFiles.getRootDirectory())
print(help('modules'))
print('\n'.join(sys.path))

import h2o
from pysparkling import *
# Initiate H2OContext
hc = H2OContext.getOrCreate(spark)

# Stop H2O and Spark services
h2o.cluster().shutdown()
spark.stop()
