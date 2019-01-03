package com.ljja.production.classification;

import com.ljja.mlstudy.helper.SparkFactory;
import org.apache.spark.ml.classification.NaiveBayesModel;
import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.SparkSession;

import java.util.ArrayList;
import java.util.List;

/**
 * i:9999 start:1514004990865 end:1514004990896 span:31
 * success count:10000 timespan:349427 10000/349.427
 * age:34.9427 QPS:28.6182807854001
 * <p>
 * 测试命令:java -cp ml-study-1.0.jar com.ljja.production.classification.NaiveBayesApp
 *
 * 参考资料：
 * http://blog.csdn.net/buptgshengod/article/details/53609878
 * http://blog.csdn.net/buptgshengod/article/details/73613855
 */
public class NaiveBayesApp {

    public static String modelPath = "E:/work/git-local/study_machinelearning/data/ha.pig.price.model.naivebayes";

    public static void main(String[] args) {

        SparkSession spark = SparkFactory.createLocalSparkSession();

        NaiveBayesModel model = NaiveBayesModel.load(modelPath);

        long start = System.currentTimeMillis();
        int count = 1000;

        for (int i = 0; i < count; i++) {

            long time1 = System.currentTimeMillis();

            List<VectorBean> vectorList = new ArrayList<>();
            vectorList.add(new VectorBean().RandomData());
            Dataset df = spark.createDataFrame(vectorList, VectorBean.class);
            Dataset p = model.transform(df);
            //p.show();
            p.count();

            long time2 = System.currentTimeMillis();

            System.out.println(String.format("i:%s start:%s end:%s span:%s", i, time1, time2, time2 - time1));

        }

        long end = System.currentTimeMillis();

        System.out.println(String.format("success count:%s timespan:%s QPS:%s", count, end - start, count / ((end - start) / 1000)));

        spark.stop();
    }

}
