import tensorflow as tf
import gradio

from tf.keras import layers, models

(train_images, train_labels), (
    test_images,
    test_labels,
) = tf.keras.datasets.mnist.load_data()
