import onnxruntime as ort
import functools
import cv2
import numpy as np


class Stylization:
    def __init__(self):
        self.style = None
        providers = ['DmlExecutionProvider', 'CPUExecutionProvider']
        self.ort_session = ort.InferenceSession("styles/magenta_stylization.onnx", providers=providers)

    @functools.lru_cache(maxsize=None)
    def loadImage(self, image_url):
        img = cv2.imread(image_url)
        if img is None:
            raise FileNotFoundError(f"Style image not found: {image_url}")
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = img.astype(np.float32) / 255.0
        h, w = img.shape[:2]
        scale = 256.0 / max(h, w)
        new_h, new_w = int(round(h * scale)), int(round(w * scale))
        img_resized = cv2.resize(img, (new_w, new_h))
        return img_resized[np.newaxis, ...]

    def setStyle(self, imageUrl: str):
        self.style = self.loadImage(imageUrl)

    def ApplyStyle(self, frame):
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_rgb = frame_rgb.astype(np.float32)[np.newaxis, ...] / 255.0
        outputs = self.ort_session.run(None, {
            "placeholder": frame_rgb,
            "placeholder_1": self.style
        })
        
        stylized = outputs[0][0]
        return stylized
