# -*- coding: utf-8 -*-

import argparse
import os

import pandas as pd
import tensorflow as tf

TRAIN_URL = "http://download.tensorflow.org/data/iris_training.csv"
TEST_URL = "http://download.tensorflow.org/data/iris_test.csv"
CSV_COLUMN_NAMES = ['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Species']
SPECIES = ['Setosa', 'Versicolor', 'Virginica']
model_dir = "C:/test/tf-model"
data_cache_dir = "C:/test/tf-data"
tf_summary_dir = "C:/test/tf-log"
test_ckpt_file = "C:/test/tf-ckpt-test/test.ckpt"
export_model_dir = "C:/test/tensorflow-model-server/demo"

# 写入日志目录
# tensorboard --logdir c:/test/tf-log
# tf.summary.FileWriter("c:/test/tf-log", tf.Session.graph)

parser = argparse.ArgumentParser()
parser.add_argument('--batch_size', default=100, type=int, help='batch size')
parser.add_argument('--train_steps', default=1000, type=int, help='number of training steps')


def load_data(label_name='Species'):
    if not os.path.exists(data_cache_dir):
        os.mkdir(data_cache_dir)

    train_path = tf.keras.utils.get_file(fname=TRAIN_URL.split('/')[-1], origin=TRAIN_URL, cache_dir=data_cache_dir)
    print("train_path=", train_path)
    train = pd.read_csv(filepath_or_buffer=train_path, names=CSV_COLUMN_NAMES, header=0)
    train_features, train_label = train, train.pop(label_name)

    test_path = tf.keras.utils.get_file(TEST_URL.split('/')[-1], origin=TEST_URL, cache_dir=data_cache_dir)
    print("test_path=", test_path)
    test = pd.read_csv(test_path, names=CSV_COLUMN_NAMES, header=0)
    test_features, test_label = test, test.pop(label_name)

    return (train_features, train_label), (test_features, test_label)


def train_input_fn(features, labels, batch_size):
    return tf.data \
        .Dataset \
        .from_tensor_slices((dict(features), labels)) \
        .shuffle(buffer_size=1000) \
        .repeat(count=None) \
        .batch(batch_size) \
        .make_one_shot_iterator() \
        .get_next()


def eval_input_fn(features, labels=None, batch_size=None):
    features = dict(features)

    if labels is None:
        inputs = features
    else:
        inputs = (features, labels)

    return tf \
        .data \
        .Dataset \
        .from_tensor_slices(inputs) \
        .batch(batch_size) \
        .make_one_shot_iterator() \
        .get_next()


def tf_saver_restore():
    tf.reset_default_graph()
    v1 = tf.get_variable("v1", shape=[3])
    v2 = tf.get_variable("v2", shape=[5])
    saver = tf.train.Saver()
    with tf.Session() as sess:
        saver.restore(sess, test_ckpt_file)
        print("Model restored.")
        print("v1 : %s" % v1.eval())
        print("v2 : %s" % v2.eval())

    from tensorflow.python.tools import inspect_checkpoint as chkp
    print("print ckpt...")
    chkp.print_tensors_in_checkpoint_file(test_ckpt_file, tensor_name='', all_tensors=True)


def tf_saver_save():
    v1 = tf.get_variable("v1", shape=[3], initializer=tf.zeros_initializer)
    v2 = tf.get_variable("v2", shape=[5], initializer=tf.zeros_initializer)

    inc_v1 = v1.assign(v1 + 1)
    dec_v2 = v2.assign(v2 - 1)

    init_op = tf.global_variables_initializer()

    saver = tf.train.Saver()

    with tf.Session() as sess:
        sess.run(init_op)

        inc_v1.op.run()
        dec_v2.op.run()

        print(v1.eval())
        print(v2.eval())

        # 保存变量
        save_path = saver.save(sess, test_ckpt_file)

        print("Model saved in path: %s" % save_path)


feature_spec = {
    'SepalLength': tf.FixedLenFeature(dtype=tf.float32, shape=[1]),
    'SepalWidth': tf.FixedLenFeature(dtype=tf.float32, shape=[1]),
    'PetalLength': tf.FixedLenFeature(dtype=tf.float32, shape=[1]),
    'PetalWidth': tf.FixedLenFeature(dtype=tf.float32, shape=[1])
}


def serving_input_receiver_fn():
    serialized_tf_example = tf.placeholder(dtype=tf.string, name='input_example_tensor')
    receiver_tensors = {'examples': serialized_tf_example}
    print("receiver_tensors=", receiver_tensors)

    features = tf.parse_example(serialized_tf_example, feature_spec)
    print("features=", features)

    return tf.estimator.export.ServingInputReceiver(features, receiver_tensors)


def main(argv):
    args = parser.parse_args(argv[1:])

    (train_x, train_y), (test_x, test_y) = load_data()

    my_feature_columns = []
    for key in train_x.keys():
        my_feature_columns.append(tf.feature_column.numeric_column(key=key))

    my_checkpointing_config = tf.estimator.RunConfig(
        save_checkpoints_secs=10,  # 每10秒保存一次检查点
        keep_checkpoint_max=10,  # 最多保存10个检查点
    )
    classifier = tf.estimator.DNNClassifier(feature_columns=my_feature_columns,
                                            hidden_units=[10, 10],
                                            n_classes=3,
                                            model_dir=model_dir,
                                            config=my_checkpointing_config)

    print("classifier.model_dir=", classifier.model_dir)

    print("train")
    classifier.train(
        input_fn=lambda: train_input_fn(
            train_x,
            train_y,
            args.batch_size),
        steps=args.train_steps)

    print("evaluate")
    eval_result = classifier.evaluate(
        input_fn=lambda: eval_input_fn(
            test_x,
            test_y,
            args.batch_size))
    print('\nTest set accuracy: {accuracy:0.3f}\n'.format(**eval_result))

    print("predict")
    expected = ['Setosa', 'Versicolor', 'Virginica']
    predict_x = {
        'SepalLength': [5.1, 5.9, 6.9],
        'SepalWidth': [3.3, 3.0, 3.1],
        'PetalLength': [1.7, 4.2, 5.4],
        'PetalWidth': [0.5, 1.5, 2.1],
    }
    predictions = classifier.predict(
        input_fn=lambda: eval_input_fn(
            predict_x,
            labels=None,
            batch_size=args.batch_size))

    for pred_dict, expec in zip(predictions, expected):
        template = ('\nPrediction is "{}" ({:.1f}%), expected "{}"')
        class_id = pred_dict['class_ids'][0]
        probability = pred_dict['probabilities'][class_id]
        print(template.format(SPECIES[class_id], 100 * probability, expec))

    # 导出模型
    # tensorflow_model_server --model_name=demo --model_base_path=/mnt/c/test/tensorflow-model-server/demo
    # tf.estimator.Estimator.export_savedmodel(export_model_dir, serving_input_receiver_fn)
    classifier.export_savedmodel(export_model_dir, serving_input_receiver_fn)


if __name__ == '__main__':
    # shutil.rmtree(model_dir)
    # shutil.rmtree(data_cache_dir)
    # shutil.rmtree(tf_summary_dir)

    tf.logging.set_verbosity(tf.logging.INFO)

    # 检查点保存恢复测试
    # tf_saver_save()
    # tf_saver_restore()
    # tf.summary.FileWriter(tf_summary_dir, tf.Session().graph)

    tf.app.run(main)

    # build = tf.saved_model.builder.SavedModelBuilder(export_model_dir)
    # build.add_meta_graph()
    # build.save()
