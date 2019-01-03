# -*- coding: utf-8 -*-

import numpy as np
import tensorflow as tf

clusterSpec = tf.train.ClusterSpec({"worker": ["localhost:2222", "localhost:3333"]})

server = tf.train.Server(clusterSpec, job_name="worker", task_index=1)

server.join()
