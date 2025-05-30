from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Defining model architecture
model = Sequential([
    Dense(16, activation='relu', input_shape=(4,)),
    Dense(8, activation='relu'),
    Dense(1, activation='sigmoid')
])

# Summary of model
model.summary()

