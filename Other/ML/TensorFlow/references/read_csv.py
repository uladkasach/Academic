###########################################################
## Logistic Regression with Stochastic Gradient Descent Training over MNIST training set
############################################################
import tensorflow as tf
import numpy as np
import sys


filename_queue = tf.train.string_input_producer(["../../features/output/featured_data_sub.csv"])


################################################
## Define data variables
################################################
reader = tf.TextLineReader(skip_header_lines=1)
key, row_value = reader.read(filename_queue)
record_defaults = [[1], [1], [1], [.1], [.1], [0.1], [0.1], [0.1], [0.1]] # Default values, in case of empty columns. Also specifies the type of the decoded result.
col1, col2, col3, col4, col5, col6, col7, col8, col9 = tf.decode_csv(row_value, record_defaults=record_defaults)
features = tf.pack([col4, col5, col6, col7, col8, col9])
'''
results = tf.decode_csv(row_value, record_defaults=record_defaults)
print(len(results)); ## len(list)
'''
labels = tf.pack([col3])

with tf.Session() as sess:
    # Start populating the filename queue.
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(coord=coord)

    #for i in range(1200):
        # Retrieve a single instance:
    print(col1);
    example = sess.run([features])
    print(example);

    coord.request_stop()
    coord.join(threads)
