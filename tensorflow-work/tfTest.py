import tensorflow as tf

init = tf.global_variables_initializer()

with tf.Session() as client:
    client.run(init)
    print(client.list_devices())
    
client.close()
