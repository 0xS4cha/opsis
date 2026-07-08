import functools
import os

from matplotlib import gridspec
import matplotlib.pylab as plt
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub


class Stylization:
    def __init__(self):
        pass

    def loadImage(self, imageUrl):
        image_path = tf.keras.utils.get_file(os.path.basename(imageUrl)[-128:], imageUrl)
        img = tf.io.decode_image(
            tf.io.read_file(image_path),
            channels=3, dtype=tf.float32)[tf.newaxis, ...]
        # img = tf.image.resize(img, image_size, preserve_aspect_ratio=True)
        return img

    def setStyle(self, imageUrl: str):
        pass

    def ApplyStyle(self, frame):
        pass
    