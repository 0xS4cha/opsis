import tensorflow as tf
import functools
import tensorflow_hub as hub
import cv2
import numpy as np


class Stylization:
    def __init__(self):
        self.style = ""
        self.hub_module = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')

    @functools.lru_cache(maxsize=None)
    def loadImage(self, image_url):
        img = tf.io.decode_image(
            tf.io.read_file(image_url),
            channels=3, dtype=tf.float32)[tf.newaxis, ...]
        img = tf.image.resize(img, (256, 256), preserve_aspect_ratio=True)
        return img

    def setStyle(self, imageUrl: str):
        self.style = self.loadImage(imageUrl)

    def ApplyStyle(self, frame):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = frame.astype(np.float32)[np.newaxis, ...] / 255.0

        outputs = self.hub_module(tf.constant(frame), tf.constant(self.style))
        stylized = outputs[0][0]
        return stylized.numpy()
