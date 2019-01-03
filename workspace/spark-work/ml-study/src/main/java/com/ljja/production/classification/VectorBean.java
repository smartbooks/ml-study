package com.ljja.production.classification;

import org.apache.spark.ml.linalg.Vector;
import org.apache.spark.ml.linalg.Vectors;

import java.io.Serializable;

public class VectorBean implements Serializable {

    public Vector scaledFeatures;

    public VectorBean RandomData() {
        scaledFeatures = Vectors.dense(new double[]{0.0, 0.4807692307692308, 0.3989898989898988, 0.08961474036850924, 0.14285714285714285, 0.17333333333333348, 0.05893536121672996, 0.0918367346938774, 0.017923362175525398});

        return this;
    }

    public Vector getScaledFeatures() {
        return scaledFeatures;
    }

    public void setScaledFeatures(Vector scaledFeatures) {
        this.scaledFeatures = scaledFeatures;
    }
}
