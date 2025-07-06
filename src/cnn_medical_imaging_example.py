"""
Contoh kode CNN untuk klasifikasi pencitraan medis (X-ray).
"""

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

model = Sequential([
    Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(224, 224, 1)),
    MaxPooling2D(pool_size=(2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(1, activation='sigmoid')  # 0 = normal, 1 = pneumonia (misal)
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# model.fit(x_train, y_train, epochs=10, validation_data=(x_val, y_val))
