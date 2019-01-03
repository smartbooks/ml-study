package com.ljja.mlstudy.helper

import org.apache.log4j.{Level, Logger}
import org.apache.spark.SparkConf
import org.apache.spark.sql.SparkSession
import org.apache.spark.streaming.{Seconds, StreamingContext}

object SparkFactory {

  val master = "local[*]"
  val hadoop_home_dir = "D:/tool/hadoop-2.7.3"
  val warehouse_dir = "E:/work/git-local/study_machinelearning/data/spark-warehouse"

  def createSparkSession(): SparkSession = {
    val spark = SparkSession.builder().getOrCreate()
    spark.conf.set("spark.sql.broadcastTimeout", 60 * 30)
    spark
  }

  def createLocalSparkSession(): SparkSession = {
    initLocalEnv()
    SparkSession
      .builder()
      .master(master)
      .config("spark.sql.warehouse.dir", warehouse_dir)
      .getOrCreate()
  }

  def createLocalStreamingContext(sparkTimeSpan: Int = 5): StreamingContext = {
    initLocalEnv()
    val conf = new SparkConf().setMaster(master)
    new StreamingContext(conf, Seconds(sparkTimeSpan))
  }

  def initLocalEnv(): Unit = {
    Logger.getLogger("org").setLevel(Level.ERROR)
    System.setProperty("hadoop.home.dir", hadoop_home_dir)
  }

}
