###########################################################
## Logistic Regression with Stochastic Gradient Descent Training over MNIST training set
##       https://www.tensorflow.org/versions/r0.9/tutorials/mnist/beginners/index.html
############################################################
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

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

cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1])) ## Cost function
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy) ## Gradient Descent

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
  batch_xs, batch_ys = mnist.train.next_batch(100)
  sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
    
    
################################
## Evaluate Model
################################
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))