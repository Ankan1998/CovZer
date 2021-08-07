import tensorflow as tf

def model_fn():
# Used Sequential
    model=tf.keras.Sequential()
    model.add(tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(64, 64, 3)))
    model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2), strides=(2, 2), padding="valid"))
    model.add(tf.keras.layers.Conv2D(64, (3,3), activation='relu'))
    model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2), strides=(2, 2), padding="valid"))
    model.add(tf.keras.layers.Conv2D(128, (3,3), activation='relu'))
    model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2), strides=(2, 2), padding="valid"))
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(128, activation='relu'))
    model.add(tf.keras.layers.Dropout(.1, input_shape=(128,)))
    model.add(tf.keras.layers.Dense(4, activation='softmax'))

    print(model.summary())

    return model