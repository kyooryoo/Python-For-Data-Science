# Neural Network is modeled after biological neural network and attempts to
# allow computer to learn like humans do - reinforcement learning
# NN is used for Pattern Recognition, Time Series Prediction, Signal Processing
# Anomaly Detection and Intelligent Control such self driving vehicles

# a perceptron consists of one or more inputs, a processor and a single output
# which follows the feed forward model by receieve inputs, weight inputs, sum
# inputs and generate output. The output is generated by passing that sum
# through an activation function to tell the perception to filr ot not, in case
# of a simple binary output scenario. Bias could be added as an extra input to
# avoid some issues such as having zero as output and no proper binary output.
# For training the perceptron, we privide inputs for which there is a known
# answer, then compute the error, adjust all weights according to the error,
# and repeat all these steps. Layers of perceptron are networked to function.
# There are input, output and hidden layers in between. Deep learning use many
# hidden layers which makes the network deep, which may contain hundreds layers.

# TensorFlow is a NN library which creates data flow graphs. The arrays passed
# along from layer of nodes to layer of nodes is known as a Tensor. Graph 
# Session method is customizable, while SciKit-Learn type interface with
# Contrib.Learn method is easier to use but has less customization capability.

# Install TensorFlow in iOS (in terminal):
# sudo easy_install pip
# sudo pip --upgrade virtualenv
# virtualenv --system-site-packages ~/tensorflow
# cd ~/tensorflow
# source ./bin/activate 
# easy_install pip
# pip install --upgrade tensorflow

# Verify installation (in terminal):
# python
# import tensorflow as tf
# hello = tf.constant('Hello')
# sess = tf.Session()
# print(sess.run(hello))

# Deactivate or Uninstall:
# (targetDidrectory)$ deactivate
# rm -r ~/tensorflow