import tensorflow as tf
import matplotlib.pyplot as plt
import mne

hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))