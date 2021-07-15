import tensorflow as tf
# Model using custom class
# class ConvNet(tf.keras.Model):
#
#
#   def __init__(self):
#     super().__init__()
#     self.conv1=tf.keras.layers.Conv2D(64, (3,3), activation='relu', input_shape=(64, 64, 3))
#     self.mpool=tf.keras.layers.MaxPooling2D(pool_size=(2, 2), strides=None, padding="valid")
#     self.conv2=tf.keras.layers.Conv2D(32, (3,3), activation='relu')
#     self.flat=tf.keras.layers.Flatten()
#     self.dense1=tf.keras.layers.Dense(32)
#     self.drop=tf.keras.layers.Dropout(.1, input_shape=(32,))
#     self.out=tf.keras.layers.Dense(1, activation='sigmoid')
#
#   def call(self,inputs):
#     x=self.conv1(inputs)
#     x=self.mpool(x)
#     x=self.conv2(x)
#     x=self.mpool(x)
#     x=self.flat(x)
#     x=self.dense1(x)
#     x=self.drop(x)
#     x=self.out(x)
#
#     return x
import cv2

#model = ConvNet()
img_p = r'test.png'
img = cv2.imread(img_p)
img = cv2.resize(img,(64,64))
print(img.shape)
model = tf.keras.models.load_model(r'./covid_model')
p = model(img)
print(p)
#
# print(model.summary())