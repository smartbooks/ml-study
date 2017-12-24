package com.ljja.production.http;

import com.ljja.mlstudy.helper.SparkFactory;
import com.ljja.production.classification.VectorBean;
import org.apache.spark.ml.classification.NaiveBayesModel;
import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.SparkSession;
import org.eclipse.jetty.server.Request;
import org.eclipse.jetty.server.handler.AbstractHandler;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class NaiveBayesHandler extends AbstractHandler {

    private final String modelPath = "E:/work/git-local/study_machinelearning/data/ha.pig.price.model.naivebayes";
    private NaiveBayesModel model = null;
    private SparkSession spark = null;

    @Override
    protected void doStart() throws Exception {
        super.doStart();
        spark = SparkFactory.createLocalSparkSession();
        model = NaiveBayesModel.load(modelPath);
    }

    @Override
    protected void doStop() throws Exception {
        super.doStop();
        spark.stop();
    }

    @Override
    public void handle(String target, Request baseRequest, HttpServletRequest request, HttpServletResponse response)
            throws IOException, ServletException {
        try {

            response.setContentType("text/html;charset=utf-8");
            response.setStatus(HttpServletResponse.SC_OK);
            baseRequest.setHandled(true);

            long start = System.currentTimeMillis();

            List<VectorBean> vectorList = new ArrayList<>();
            vectorList.add(new VectorBean().RandomData());
            Dataset df = spark.createDataFrame(vectorList, VectorBean.class);
            Dataset p = model.transform(df);

            long end = System.currentTimeMillis();

            response.getWriter().println(String.format("start:%s end:%s span:%s data_count:%s, data:%s",
                    start,
                    end,
                    end - start,
                    p.count(),
                    p.head()));

        } catch (Exception e) {
            e.printStackTrace();
            response.getWriter().println(e.getMessage());
        }
    }
}
