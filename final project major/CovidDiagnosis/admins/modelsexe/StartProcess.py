from django.conf import settings
import os
import numpy as np
class MyModelStartExecution:
    def startProcess(self,filepath):
        print("Am working")
        import cv2
        import tensorflow as tf
        categories = ["covid19_scan", "normal_scan"]
        def prepare(filepath):
            IMG_SIZE = 224
            img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
            new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
            return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)

        # modelpath = settings.MEDIA_ROOT + "\\" + 'covid19_pneumonia_detection_cnn.model'
        modelpath = os.path.join(settings.MEDIA_ROOT, 'model1.h5')
        # modelpath = 'covid19.model'
        new_model = tf.keras.models.load_model(modelpath)  # provides the path of your trained CNN model
        path = os.path.join(settings.MEDIA_ROOT, 'ctscans', filepath)
        from keras.preprocessing import image
        from keras.models import load_model
        #new_model = load_model(modelpath)
        new_model.summary()
        test_image = image.load_img(path, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = new_model.predict(test_image)
        print(result[0][0])
        if result[0][0] == 0:

            prediction = 'Patient is affected with Corona'
        else:
            prediction = 'Patient is Healthy'

        return prediction
