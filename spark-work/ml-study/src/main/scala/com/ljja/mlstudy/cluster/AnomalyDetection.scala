package com.ljja.mlstudy.cluster

import java.io.FileOutputStream

import com.ljja.mlstudy.helper.{SparkFactory, ThrowablePrint}
import org.apache.spark.mllib.clustering.{KMeans, KMeansModel}
import org.apache.spark.rdd.RDD
import org.apache.spark.mllib.linalg._

/*
http://blog.csdn.net/qq1010885678/article/details/51354486
http://blog.csdn.net/stevekangpei/article/details/76549267
http://shiyanjun.cn/archives/1388.html
 */
object AnomalyDetection {

  val outputPMML = "C:/test/kddcup99/pmml-k-means.pmml"
  val inputPath = "C:/test/kddcup99/kddcup.data_10_percent_corrected"

  def main(args: Array[String]): Unit = {
    try {

      val spark = SparkFactory.createLocalSparkSession()

      val rawData = spark.sparkContext.textFile(inputPath)

      //根据类别查看统计信息,各个类别下有多少数据
      //rawData
      //  .map(_.split(",").last)
      //  .countByValue()
      //  .toSeq
      //  .sortBy(_._2)
      //  .reverse
      //  .foreach(println)

      val labelsAndData = rawData.map { line =>
        //buffer是一个可变列表
        val buffer = line.split(",").toBuffer
        //下标1-3的元素
        buffer.remove(1, 3)
        //最后一个元素为label
        val label = buffer.remove(buffer.length - 1)
        //转换为Vector
        val vector = Vectors.dense(buffer.map(_.toDouble).toArray)
        (label, vector)
      }

      //数据只用到values部分
      val data = labelsAndData.values.cache()

      //取不同k值观察模型优劣
      (500 to 1000 by 10)
        .map { k => (k, clusteringScore(data, k)) }
        .foreach(f => println(s"k:${f._1} mean:${f._2._1} std:${f._2._2}"))

      /**
        * k	score
        * 900	55.3968976
        * 840	62.85252988
        * 1000	65.78081583
        * 870	76.5222759
        * 820	82.22798953
        */
      println("success")

    } catch {
      case e: Throwable => ThrowablePrint.printStackTrace(e)
    }
  }

  /**
    * 计算两个向量之间的距离
    *
    * @param a 向量1
    * @param b 向量2
    *          欧式距离:空间上两个点的距离=两个向量相应元素的差的平方和的平方根
    **/
  def distance(a: Vector, b: Vector) = {
    //求平方根
    scala.math.sqrt(
      //将两个向量合并
      a.toArray.zip(b.toArray)
        //两个向量中的每个值相减
        .map(d => d._1 - d._2)
        //相间的值平方
        .map(d => d * d)
        //之后相加
        .sum)
  }

  /**
    * 计算数据点到聚类中心质心的距离
    *
    * @param datum 数据点
    * @param model kmeans模型
    **/
  def distToCentrolid(datum: Vector, model: KMeansModel) = {
    //数据点所属聚类中心
    val cluster = model.predict(datum)

    //数据点所属聚类中心的质心向量
    val centrolid = model.clusterCenters(cluster)

    //计算数据点到质心的距离
    distance(centrolid, datum)
  }

  /**
    * 根据各个数据点到该数据点聚类中心质心的距离来判断该模型优劣
    *
    * @param data 样本数据
    * @param k    k值
    **/
  def clusteringScore(data: RDD[Vector], k: Int) = {

    val kmeans = new KMeans()

    //设置k值
    kmeans.setK(k)

    //随机数种子
    kmeans.setSeed(Math.PI.toLong)

    //最大迭代次数
    kmeans.setMaxIterations(50)

    //初始模式:random  k-means||
    kmeans.setInitializationMode("k-means||")

    //每次迭代步数
    kmeans.setInitializationSteps(2)

    //设置迭代过程中,质心的最小移动值,默认为1.0e-4
    kmeans.setEpsilon(1.0e-6)

    val model = kmeans.run(data)

    //model.toPMML(new FileOutputStream(outputPMML))

    //计算样本数据到其各自质心的记录的均值,均值越小聚类越均衡
    val pos = data.map { m => distToCentrolid(m, model) }.persist()

    val mean = pos.mean()

    val std = pos.stdev()

    pos.unpersist()

    (mean, std)
  }

}
