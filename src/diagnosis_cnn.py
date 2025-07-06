"""
Studi Kasus 1: Diagnosis Penyakit Berbasis Pencitraan Medis dengan CNN
"""

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def build_model():
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 1)),
        MaxPooling2D(2, 2),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D(2, 2),
        Flatten(),
        Dense(128, activation='relu'),
        Dropout(0.5),
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

# Dummy datagen example (real data should be added manually)
def create_datagen():
    datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)
    return datagen

# Model can be trained using:
# model.fit(train_generator, epochs=10, validation_data=val_generator)
