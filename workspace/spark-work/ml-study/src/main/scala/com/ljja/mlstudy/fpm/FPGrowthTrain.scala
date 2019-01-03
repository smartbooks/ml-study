package com.ljja.mlstudy.fpm

import com.ljja.mlstudy.helper.{SparkFactory, ThrowablePrint}
import org.apache.spark.ml.fpm.FPGrowth

/**
  * 频繁项挖掘-关联规则分析
  *
  * 示例数据：
  * 频繁项集合
  * +---------+----+
  * |    items|freq|
  * +---------+----+
  * |      [1]|   3|
  * |      [2]|   3|
  * |   [2, 1]|   3|
  * |      [5]|   2|
  * |   [5, 2]|   2|
  * |[5, 2, 1]|   2|
  * |   [5, 1]|   2|
  * +---------+----+
  *
  * 关联规则
  * +----------+----------+------------------+
  * |antecedent|consequent|        confidence|
  * +----------+----------+------------------+
  * |    [2, 1]|       [5]|0.6666666666666666|
  * |    [5, 1]|       [2]|               1.0|
  * |       [2]|       [1]|               1.0|
  * |       [2]|       [5]|0.6666666666666666|
  * |       [5]|       [2]|               1.0|
  * |       [5]|       [1]|               1.0|
  * |       [1]|       [2]|               1.0|
  * |       [1]|       [5]|0.6666666666666666|
  * |    [5, 2]|       [1]|               1.0|
  * +----------+----------+------------------+
  *
  * 效果预测
  * +------------+----------+
  * |       items|prediction|
  * +------------+----------+
  * |   [1, 2, 5]|        []|
  * |[1, 2, 3, 5]|        []|
  * |      [1, 2]|       [5]|
  * +------------+----------+
  *
  */
object FPGrowthTrain {

  def main(args: Array[String]): Unit = {
    try {

      val spark = SparkFactory.createLocalSparkSession()

      import spark.implicits._

      val dataset = spark.createDataset(Seq(
        "1 2 5",
        "1 2 3 5",
        "1 2")
      ).map(t => t.split(" ")).toDF("items")

      val fpgrowth = new FPGrowth()
        .setItemsCol("items")
        .setMinSupport(0.5)
        .setMinConfidence(0.6)

      val model = fpgrowth.fit(dataset)

      println("频繁项集合")
      model.freqItemsets.show()

      println("关联规则")
      model.associationRules.show()

      println("效果预测")
      model.transform(dataset).show()

      println("succcess")

    } catch {
      case e: Throwable => ThrowablePrint.printStackTrace(e)
    }
  }

}
