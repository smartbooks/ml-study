package com.ljja.mlstudy.classification

import com.ljja.mlstudy.helper.{SparkFactory, ThrowablePrint}
import org.apache.spark.ml.classification.NaiveBayes
import org.apache.spark.ml.evaluation.MulticlassClassificationEvaluator
import org.apache.spark.ml.feature.{MinMaxScaler, VectorAssembler}
import org.apache.spark.sql.functions.col
import org.apache.spark.sql.types.{DoubleType, StringType, StructField, StructType}

/**
  * 分类-朴素贝叶斯-训练
  */
object NaiveBayesTrain {

  val modelPath = "E:/work/git-local/study_machinelearning/data/ha.pig.price.model.naivebayes"
  val trainFile = "E:/work/git-local/study_machinelearning/data/ha.pig.price.train.csv"

  def main(args: Array[String]): Unit = {
    try {

      val spark = SparkFactory.createLocalSparkSession()

      val customSchema = new StructType(Array(
        StructField("year", DoubleType, true), //年
        StructField("week", DoubleType, true), //周
        StructField("pig_price", DoubleType, true), //活猪价格
        StructField("bean_pulp_price", DoubleType, true), //豆粕价格
        StructField("chance", DoubleType, true), //猪周期
        StructField("yumi", DoubleType, true), //玉米
        StructField("xiaomaifu", DoubleType, true), //小麦麸
        StructField("yufen", DoubleType, true), //鱼粉
        StructField("siliao", DoubleType, true), //育肥猪配合饲料
        StructField("zhurou", DoubleType, true))) //猪肉

      // 原始数据
      val df = spark.read
        .option("header", true)
        .schema(customSchema)
        .csv(trainFile)

      df.printSchema()

      // 字段转换成特征向量
      val assembler = new VectorAssembler()
        .setInputCols(Array("year", "week", "bean_pulp_price", "pig_price", "yumi", "xiaomaifu", "yufen", "siliao", "zhurou"))
        .setOutputCol("features")
        .transform(df)

      assembler.show(false)

      val scaler = new MinMaxScaler()
        .setInputCol("features")
        .setOutputCol("scaledFeatures")
        .fit(assembler)
        .transform(assembler)

      scaler.show(false)

      val Array(trainDF, testDF) = scaler.randomSplit(Array(0.8, 0.2), scaler.count())

      val model = new NaiveBayes()
        .setLabelCol("chance")
        .setFeaturesCol("scaledFeatures")
        .setPredictionCol("pred")
        .setProbabilityCol("prob")
        .fit(trainDF)

      model.write.overwrite().save(modelPath)

      val predictions = model.transform(testDF)

      predictions.printSchema()
      predictions.orderBy(col("year").desc, col("week").desc).show(500, false)

      val evaluator = new MulticlassClassificationEvaluator()
        .setLabelCol("chance")
        .setPredictionCol("pred")

      println(
        s"f1=${evaluator.setMetricName("f1").evaluate(predictions)}" +
          s" accuracy=${evaluator.setMetricName("accuracy").evaluate(predictions)}" +
          s" weightedPrecision=${evaluator.setMetricName("weightedPrecision").evaluate(predictions)}" +
          s" weightedRecall=${evaluator.setMetricName("weightedRecall").evaluate(predictions)}")

      println("success")

    } catch {
      case e: Throwable => ThrowablePrint.printStackTrace(e)
    }
  }

}
