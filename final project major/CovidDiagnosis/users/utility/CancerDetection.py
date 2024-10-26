import os
import cv2
import tensorflow as tf
from django.conf import settings


class LuncgWeights:
    def predict_from_image(self, filepath):
        categories = ["Cancer","Normal"]

        def prepare(filepath):
            IMG_SIZE = 150
            img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
            new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
            return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)

        modelpath = os.path.join(settings.MEDIA_ROOT, 'lungweights', 'lungcancer.h5')
        model = tf.keras.models.load_model(modelpath)  # provides the path of your trained CNN model
        path = os.path.join(settings.MEDIA_ROOT, 'lungs', filepath)
        print("FIle Path =", path)
        prediction = model.predict([prepare(path)])
        print("Predictin is ",prediction)
        return categories[int(prediction[0][0])]
