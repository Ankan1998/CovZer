from tensorflow import keras
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

def prediction_fn(img_path):
    model_classification = keras.models.load_model(r'C:\Users\Ankan\Desktop\Github\CovZer\webapp\best_weightv2')
    #im_path='/content/drive/MyDrive/PROJECTS/Flutter_ML_Covid_Xray_Classification/dataset/Covid/COVID-3596.png'
    img = image.load_img(img_path, target_size=(128, 128))
    img_array = image.img_to_array(img)
    img_batch = np.expand_dims(img_array, axis=0)
    img_batch /= 255.0
    tensor = tf.convert_to_tensor(img_batch)
    prediction = model_classification.predict(tensor)
    return np.argmax(prediction, axis=0)
