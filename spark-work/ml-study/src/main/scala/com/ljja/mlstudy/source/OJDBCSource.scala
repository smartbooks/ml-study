package com.ljja.mlstudy.source

import com.ljja.mlstudy.helper.SparkFactory
import org.apache.spark.sql.SaveMode
import org.apache.spark.sql.types._

object OJDBCSource {

  def main(args: Array[String]): Unit = {
    try {

      val spark = SparkFactory.createLocalSparkSession()

      //读取本地目录压缩数据
      val d = spark.read.parquet("spark-warehouse/simple_log")
      d.show(false)
      println(d.count())

      //读取原始LOG数据
      val path = "C:/work/doc-work/统计需求/statistic20171219.log"

      val schema = StructType(Array(
        StructField("date", StringType, true),
        StructField("uid", LongType, true),
        StructField("page", StringType, true),
        StructField("version", StringType, true),
        StructField("ip", StringType, true),
        StructField("_c5", StringType, true),
        StructField("_c6", StringType, true),
        StructField("_c7", StringType, true),
        StructField("_c8", StringType, true),
        StructField("phone_model", StringType, true),
        StructField("_c10", StringType, true),
        StructField("_c11", StringType, true),
        StructField("_c12", StringType, true),
        StructField("_c13", StringType, true),
        StructField("resolution", StringType, true),
        StructField("_c15", StringType, true),
        StructField("_c16", StringType, true),
        StructField("_c17", StringType, true),
        StructField("_c18", StringType, true),
        StructField("_c19", StringType, true),
        StructField("_c20", StringType, true)))

      val df = spark.read
        .format("com.databricks.spark.csv")
        .option("header", false)
        .option("inferSchema", "true")
        .option("delimiter", "\t")
        .schema(schema)
        .csv(path)

      df.printSchema()
      df.show(false)

      //写入数据到ORACLE数据测试
      df.write
        .mode(SaveMode.Overwrite)
        .format("jdbc")
        .option("url", "jdbc:oracle:thin:@//host:1521/ORCL")
        .option("dbtable", "simple_log")
        .option("user", "root")
        .option("password", "root")
        .option("driver", "oracle.jdbc.driver.OracleDriver")
        .save()

      //写入到本地仓库
      df.write.saveAsTable("simple_log")

      println("success")

    } catch {
      case e: Throwable => e.printStackTrace()
    }
  }

}
