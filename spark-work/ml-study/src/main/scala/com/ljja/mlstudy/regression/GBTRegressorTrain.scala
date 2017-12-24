package com.ljja.mlstudy.regression

import com.ljja.mlstudy.helper.{SparkFactory, ThrowablePrint}
import org.apache.spark.ml.Pipeline
import org.apache.spark.ml.evaluation.RegressionEvaluator
import org.apache.spark.ml.feature.{MinMaxScaler, VectorAssembler, VectorIndexer}
import org.apache.spark.ml.regression.{GBTRegressionModel, GBTRegressor}
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._

/**
  * 回归-决策树回归-训练
  *
  * 根据豆粕价格预测活猪价格走势
  * 数据来源：http://www.hnxmy.gov.cn/price/GetListPrice.html
  * 预测结果：数值型
  */
object GBTRegressorTrain {

  val modelPath = "E:/work/git-local/study_machinelearning/data/ha.pig.price.model.gbt"
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
        .setInputCols(Array("week", "bean_pulp_price", "yumi", "xiaomaifu", "yufen", "siliao", "zhurou"))
        .setOutputCol("features")
        .transform(df)
        .cache()

      val Array(trainDF, testDF) = assembler.randomSplit(Array(0.9, 0.1), assembler.count())

      // 训练GBT模型
      val gbt = new GBTRegressor()
        .setLabelCol("pig_price")
        .setFeaturesCol("features")
        .setImpurity("variance")
        .setLossType("squared")

      // 构建管道
      val pipeline = new Pipeline().setStages(Array(gbt))

      // 训练模型
      val model = pipeline.fit(trainDF)

      model.write.overwrite().save(modelPath)

      // 做出预测
      val predictions = model.transform(testDF)

      // 预测样本展示
      predictions.printSchema()

      val offsetUDF = udf((origin: Double, prod: Double) => origin - prod, DoubleType)

      predictions
        .orderBy(col("year").desc, col("week").desc)
        .withColumn("offset", offsetUDF(col("pig_price"), col("prediction")))
        .show(500, false)

      // 选择（预测标签，实际标签），并计算测试误差。
      val evaluator = new RegressionEvaluator()
        .setLabelCol("pig_price")
        .setPredictionCol("prediction")
        .setMetricName("rmse")

      val rmse = evaluator.evaluate(predictions)

      val gbtModel = model.stages(0).asInstanceOf[GBTRegressionModel]

      println(s"maxIter:${gbtModel.getMaxIter} maxDept:${gbtModel.getMaxDepth} tree:${gbtModel.numTrees} rmse:${rmse}")

      println("success")

    } catch {
      case e: Throwable => ThrowablePrint.printStackTrace(e)
    }
  }

}
