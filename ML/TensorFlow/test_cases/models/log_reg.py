###########################################################
## Logistic Regression with Stochastic Gradient Descent Training
############################################################
import tensorflow as tf
import numpy as np
import pandas as pd
import sys
import os

################
## Import Inputs
################
import sys
import load_data
import save_data


###########################################################################
## Define Variables
###########################################################################
###################################
## Hyper Parameters
###################################
batch_size = 100;
#########
### Exponentially decreasing learning rate
#########
starter_learning_rate = 0.05; #https://www.tensorflow.org/versions/r0.9/api_docs/python/train.html#exponential_decay
global_step = tf.Variable(0, trainable=False)
learning_rate = tf.train.exponential_decay(starter_learning_rate, global_step, 200, 0.96, staircase=True)
#learning_rate = tf.Print(learning_rate, [learning_rate], "LR");

###################################
## Data Variables / Ops
###################################
feature_batch, label_batch, key_batch = load_data.batch_input_pipeline(["../logical_functions/xor_10k.csv"], batch_size); ## Return a batch
feature_count = feature_batch.get_shape()[1]; 
label_count = label_batch.get_shape()[1]; 
with tf.Session() as sess:
    feature_count = sess.run(tf.to_int32(feature_count));
    label_count = sess.run(tf.to_int32(label_count));


###################################
## Model Variables / Ops
###################################
X = tf.placeholder(tf.float32, [None, feature_count]) ## Features
W = tf.Variable(tf.random_uniform([feature_count, label_count], 0, 10)); ## Bias
b = tf.Variable(tf.random_uniform([label_count], 0, 10)); ## Bias


#############
## Prediction
#############
def prediction(X):
    y = tf.matmul(X, W) + b;
    return y;
y = prediction(X);
y_ = tf.placeholder(tf.float32, [None, label_count]) ## True Values

#############
## Training
#############
#cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1])) ## Cost function
#cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_*y));
#cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_*tf.log(tf.clip_by_value(y,1e-10,1.0))))
#cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_*tf.log(y + 1e-10)))

softmax_prediction = tf.nn.softmax(y);
cross_entropy = tf.nn.softmax_cross_entropy_with_logits(y, y_) ## Calculates cross entropy, taking into account edge softmax cases (predicitons of 0);
cost = tf.reduce_mean(cross_entropy); 
#cost = tf.Print(cost, [cost], "Cost");
train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost, global_step=global_step) ## Gradient Descent


###############################
## Initialize variables/ops
###############################
init = tf.initialize_all_variables() ## initialization operation


################################
## Evaluate Model
################################
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))


with tf.Session() as sess:
    sess.run(init);
    
    # Start populating the filename queue.
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(coord=coord)

    #for i in range(1200):
        # Retrieve a single instance:
    #print(col1);
    #print(sess.run([results]))
    #print(example);
    
    
    epochs = 1000;
    display_ratio = 200;
    
    ## for tracking cost,acc per epoch
    training_progress = pd.DataFrame(columns =  ["epoch", "cost", "accuracy"]);
    
    for i in range(epochs):
        batch_feature, batch_label, batch_key = sess.run([feature_batch, label_batch, key_batch]);
        if(i == 0):
            print ('Init Cost : ', end = '');
            print (sess.run(cost, feed_dict={X: batch_feature, y_ : batch_label}));
        
        if(i % (epochs/display_ratio) == 0 and i != 0):
            print ('Epoch %6d' % i, end = '');
            print(' ... cost : ', end = '');
            this_cost = (sess.run(cost, feed_dict={X: batch_feature, y_ : batch_label}));
            print ('%10f' % this_cost, end = '');
            print (' -> acc : ', end = '');
            this_acc = (sess.run(accuracy, feed_dict={X: batch_feature, y_: batch_label}))
            print ('%10f' % this_acc, end = '');
            print(' - lr : ', end = ''); 
            print ('%10f' % sess.run(learning_rate), end = '');
            print('');
            training_progress.loc[i] = [i, this_cost, this_acc];

        sess.run(train_step, feed_dict={X: batch_feature, y_ : batch_label})
        """
        if(i % 5 == 0 and False):
            #print(batch_label);
            print('Cost: ', end = '');
            print (sess.run(cost, feed_dict={X: batch_feature, y_ : batch_label}));
            #print('CE: ', end = '');
            #print (sess.run(cross_entropy, feed_dict={X: batch_feature, y_ : batch_label}));
            #print('Y: ', end = '');
            #print (sess.run([y],  feed_dict={X: batch_feature, y_ : batch_label}));
            #print('SoftMax: ', end = '');
            #print (sess.run([softmax_prediction],  feed_dict={X: batch_feature, y_ : batch_label}));
            print('W: ', end = '');
            print(sess.run(W));
        """
    
    print ('Final Cost : ', end = '');
    print (sess.run(cost, feed_dict={X: batch_feature, y_ : batch_label}));
    print ('Final Learning Rate : ', end = '');
    print (sess.run(learning_rate));
    
    
    print(sess.run(softmax_prediction, feed_dict={X: batch_feature, y_ : batch_label}));
    print(batch_label);
    
    sumacc = 0;
    for i in range(10):
        batch_feature, batch_label, batch_key = sess.run([feature_batch, label_batch, key_batch]);
        acc = (sess.run(accuracy, feed_dict={X: batch_feature, y_: batch_label}))
        ## print(acc);
        sumacc += acc;
    sumacc = sumacc/10;
    print ('Average Acc : ', end = '');
    print (sumacc);
    
    coord.request_stop()
    coord.join(threads)
    
    ################################
    ## Offer to save training results
    ################################
    #print(training_progress);
    save_data.offer(training_progress)

del sess;
sys.exit();    





##########################
## Features size 28*28
## Classes 0:9
##########################

###################################
## Define Variables / Ops
###################################
x = tf.placeholder(tf.float32, [None, 784]) ## Features
W = tf.Variable(tf.zeros([784, 10])) ## Parameters 
b = tf.Variable(tf.zeros([10])) ## Bias

y = tf.nn.softmax(tf.matmul(x, W) + b) ## Predicted Values
y_ = tf.placeholder(tf.float32, [None, 10]) ## True Values

cost = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1])) ## Cost function
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cost) ## Gradient Descent

###############################
## Initialize variables/ops
###############################
init = tf.initialize_all_variables() ## initialization operation
sess = tf.Session()
sess.run(init)

#########################
## Train over 1000 epochs,
## train with stochastic batches of data
## --- Stochastic Gradient Descent
#########################
for i in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(10)
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
    
    
################################
## Evaluate Model
################################
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))