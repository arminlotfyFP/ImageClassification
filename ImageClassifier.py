#pip install -U pip setuptools wheel
#pip install tensorflow[and-cuda] opencv-python matplotlib pandas numpy
import tensorflow as tf
import os
print(tf.config.list_physical_devices("GPU"))