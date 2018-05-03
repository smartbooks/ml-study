# -*- coding: utf-8 -*-

import tensorflow as tf
import pandas as pd

TRAIN_URL = "http://download.tensorflow.org/data/iris_training.csv"
TEST_URL = "http://download.tensorflow.org/data/iris_test.csv"

CSV_COLUMN_NAMES = ['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Species']

# 写入日志目录
# tensorboard --logdir c:/test/tb
tf.summary.FileWriter("c:/test/tb", tf.Session.graph)


def load_data(label_name='Species'):
    train_path = tf.keras.utils.get_file(fname=TRAIN_URL.split('/')[-1], origin=TRAIN_URL)
    train = pd.read_csv(filepath_or_buffer=train_path, names=CSV_COLUMN_NAMES, header=0)
    train_features, train_label = train, train.pop(label_name)

    test_path = tf.keras.utils.get_file(TEST_URL.split('/')[-1], TEST_URL)
    test = pd.read_csv(test_path, names=CSV_COLUMN_NAMES, header=0)
    test_features, test_label = test, test.pop(label_name)

    return (train_features, train_label), (test_features, test_label)


my_feature_columns = [
    tf.feature_column.numeric_column(key='SepalLength'),
    tf.feature_column.numeric_column(key='SepalWidth'),
    tf.feature_column.numeric_column(key='PetalLength'),
    tf.feature_column.numeric_column(key='PetalWidth')
]

print(my_feature_columns)

classifer = tf.estimator.DNNClassifier(
    feature_columns=my_feature_columns,
    hidden_units=[10, 10],
    n_classes=3
)

# classifer.train(input_fn=lambda:train_input_fn(train_feature, train_label, args.batch_size), steps: args.train_steps)
