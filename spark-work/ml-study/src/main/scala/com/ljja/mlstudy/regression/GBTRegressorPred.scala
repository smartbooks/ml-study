package com.ljja.mlstudy.regression

import com.ljja.mlstudy.helper.{SparkFactory, ThrowablePrint}
import org.apache.spark.ml.PipelineModel
import org.apache.spark.ml.feature.VectorAssembler
import org.apache.spark.sql.SaveMode
import org.apache.spark.sql.functions.col
import org.apache.spark.sql.types.{DoubleType, StructField, StructType}

/**
  * 回归-决策树回归-预测
  */
object GBTRegressorPred {

  val predFile = "E:/work/git-local/study_machinelearning/data/ha.pig.price.pred.csv"
  val savePath = "E:/work/git-local/study_machinelearning/data/ha.pig.price.pred.result.csv"

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

      val df = spark.read
        .option("header", true)
        .schema(customSchema)
        .csv(predFile)

      df.printSchema()
      df.show(false)

      // 字段转换成特征向量
      val assembler = new VectorAssembler()
        .setInputCols(Array("week", "bean_pulp_price", "yumi", "xiaomaifu", "yufen", "siliao", "zhurou"))
        .setOutputCol("features")
        .transform(df)
        .cache()

      val model = PipelineModel.load(GBTRegressorTrain.modelPath)

      val predictions = model.transform(assembler).orderBy(col("year").desc, col("week").desc).drop("features")

      predictions.show(500, false)

      predictions.repartition(1).write.mode(SaveMode.Overwrite).option("header", true).csv(savePath)

      println("success")

    } catch {
      case e: Throwable => ThrowablePrint.printStackTrace(e)
    }
  }

}
