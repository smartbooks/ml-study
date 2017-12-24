package com.ljja.mlstudy.cf

import com.ljja.mlstudy.helper.{SparkFactory, ThrowablePrint}
import org.apache.spark.ml.evaluation.RegressionEvaluator
import org.apache.spark.ml.recommendation.ALS
import org.apache.spark.sql.types.{DoubleType, StructField, StructType}

object AlsTrain {

  val trainFile = "E:/work/git-local/study_machinelearning/data/cf.train.csv"

  def main(args: Array[String]): Unit = {
    try {

      val spark = SparkFactory.createLocalSparkSession()

      val customSchema = new StructType(Array(
        StructField("user", DoubleType, true), //user
        StructField("item", DoubleType, true), //item
        StructField("rating", DoubleType, true))) //rating

      val df = spark.read.option("header", true).schema(customSchema).csv(trainFile)

      val Array(training, test) = df.randomSplit(Array(0.8, 0.2))

      val model = new ALS()
        .setUserCol("user")
        .setItemCol("item")
        .setRatingCol("rating")
        .fit(training)

      //设置冷启动策略
      model.setColdStartStrategy("drop")

      //预测测试数据
      val predictions = model.transform(test)

      predictions.printSchema()
      predictions.show(false)

      val evaluator = new RegressionEvaluator()
        .setMetricName("rmse")
        .setLabelCol("rating")
        .setPredictionCol("prediction")

      println(s"均方根误差=${evaluator.evaluate(predictions)}")

      model.recommendForAllUsers(10).show(false)

      model.recommendForAllItems(10).show(false)

      println("success")

    } catch {
      case e: Throwable => ThrowablePrint.printStackTrace(e)
    }
  }

}
