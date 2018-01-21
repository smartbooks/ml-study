package com.ljja.mlstudy.cube

import com.ljja.mlstudy.helper.SparkFactory
import org.apache.spark.sql.Column
import org.apache.spark.sql.functions._

object CubeExample {

  def main(args: Array[String]): Unit = {
    try {

      val spark = SparkFactory.createLocalSparkSession()

      val df = spark.emptyDataFrame

      val group1 = df.groupBy("", "", "")

      val group2 = df.groupBy(df(""), df(""))

      val groupColumn = Array("A", "B", "C")
      println(groupColumn.++("D").mkString(","))
      
      df.groupBy("", groupColumn: _*)
      df.groupBy("", Array("", ""): _*)

      val selectColumn = scala.collection.mutable.ArrayBuffer[Column]()
      selectColumn.+=:(df("A"))
      selectColumn.+=:(df.col("B"))

      df.groupBy(selectColumn: _*).agg(
        sum("C"),
        count("C"),
        countDistinct("C"),
        max("C"),
        min("C"),
        avg("C"),
        stddev("C"),
        mean("C"))

    } catch {
      case e: Throwable => e.printStackTrace()
    }
  }
}