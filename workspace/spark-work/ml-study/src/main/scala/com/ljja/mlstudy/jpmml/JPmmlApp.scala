package com.ljja.mlstudy.jpmml

import java.io.FileInputStream
import java.util
import javax.xml.transform.Source
import javax.xml.transform.stream.StreamSource

import com.ljja.mlstudy.cluster.AnomalyDetection
import org.dmg.pmml.{FieldName, PMML}
import org.jpmml.evaluator.{ClusterAffinityDistribution, ModelEvaluatorFactory}
import org.jpmml.model.JAXBUtil

/*
https://github.com/jpmml
http://openscoring.io/blog/2014/05/12/testing_pmml_applications/
http://blog.csdn.net/c1481118216/article/details/74496902
https://zhuanlan.zhihu.com/p/24902234
 */
object JPmmlApp {

  def main(args: Array[String]): Unit = {
    
    val source: Source = new StreamSource(new FileInputStream(AnomalyDetection.outputPMML))

    val pmml: PMML = JAXBUtil.unmarshalPMML(source)

    val eval = ModelEvaluatorFactory.newInstance().newModelManager(pmml)

    eval.getOutputFields.iterator()

    eval.verify()

    val input = new util.HashMap[FieldName, Double]()
    input.put(new FieldName("field_0"), 0D)
    input.put(new FieldName("field_1"), 314D)
    input.put(new FieldName("field_2"), 2298D)
    input.put(new FieldName("field_3"), 0D)
    input.put(new FieldName("field_4"), 0D)
    input.put(new FieldName("field_5"), 0D)
    input.put(new FieldName("field_6"), 0D)
    input.put(new FieldName("field_7"), 0D)
    input.put(new FieldName("field_8"), 1D)
    input.put(new FieldName("field_9"), 0D)
    input.put(new FieldName("field_10"), 0D)
    input.put(new FieldName("field_11"), 0D)
    input.put(new FieldName("field_12"), 0D)
    input.put(new FieldName("field_13"), 0D)
    input.put(new FieldName("field_14"), 0D)
    input.put(new FieldName("field_15"), 0D)
    input.put(new FieldName("field_16"), 0D)
    input.put(new FieldName("field_17"), 0D)
    input.put(new FieldName("field_18"), 0D)
    input.put(new FieldName("field_19"), 3D)
    input.put(new FieldName("field_20"), 9D)
    input.put(new FieldName("field_21"), 0D)
    input.put(new FieldName("field_22"), 0D)
    input.put(new FieldName("field_23"), 0D)
    input.put(new FieldName("field_24"), 0D)
    input.put(new FieldName("field_25"), 1D)
    input.put(new FieldName("field_26"), 0D)
    input.put(new FieldName("field_27"), 0.22D)
    input.put(new FieldName("field_28"), 255D)
    input.put(new FieldName("field_29"), 255D)
    input.put(new FieldName("field_30"), 1D)
    input.put(new FieldName("field_31"), 0D)
    input.put(new FieldName("field_32"), 0D)
    input.put(new FieldName("field_33"), 0.01D)
    input.put(new FieldName("field_34"), 0D)
    input.put(new FieldName("field_35"), 0D)
    input.put(new FieldName("field_36"), 0D)
    input.put(new FieldName("field_37"), 0D)

    val output = eval.evaluate(input)

    val it = output.entrySet().iterator()

    while (it.hasNext) {
      val item = it.next()
      val k = item.getKey
      val v = item.getValue.asInstanceOf[ClusterAffinityDistribution]
      println(s"key:${k} value:${v.getEntity.getName}")
    }
  }

}
