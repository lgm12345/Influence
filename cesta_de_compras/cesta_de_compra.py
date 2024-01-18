import pandas as pd
from datetime import datetime,timedelta
import mysql.connector
from mysql.connector import Error
import pyspark
from pyspark.sql import SparkSession
from pyspark.ml.fpm import FPGrowth
from pyspark.sql.functions import collect_list
from pyspark.sql.functions import col
from pyspark import SparkConf
from pyspark.sql.types import StructType, StructField, TimestampType,StringType,IntegerType

#-------------------------------------------Instanciacao da sessao spark----------------------------------------------------#

spark = SparkSession.builder.config("spark.driver.bindAddress","0.0.0.0").config("spark.ui.port","4051").config("spark.driver.extraJavaOptions", "-Deuser.dir=/home/anaconda3/Influence/cesta_de_compras").config("spark.port.maxRetries","100").appName("Apriori").getOrCreate()


df = spark.read.parquet("fato_venda.parquet",header=True,inferSchema=True)

fp_growth = FPGrowth(itemsCol="nm_produto",minSupport=0.001,minConfidence=0.1)

cesta = df.groupBy("id_venda").agg(collect_list("nm_produto").alias("nm_produto"))

#cesta_100 = cesta.limit(100)
#cesta_100.toPandas().to_csv("cesta100.csv")



modelo = fp_growth.fit(cesta)

frequent_items = modelo.freqItemsets
print(frequent_items.count(),len(frequent_items.columns))
association_rules = modelo.associationRules
print(association_rules.count(),len(association_rules.columns))

#frequent_items.show(10)
#association_rules.show(10)


#print(cesta.select("nm_produto").distinct().show())

#cesta.toPandas().to_csv("cesta.csv")
frequent_items.toPandas().to_parquet("itens_frequentes.parquet")
association_rules.toPandas().to_parquet("regras_associacao.parquet")











