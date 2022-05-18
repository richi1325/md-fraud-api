from tensorflow import keras

def create_model(loss):
    model = keras.Sequential([
        keras.layers.Dense(31, input_dim=31, activation='relu'),
        keras.layers.Dense(16, activation='relu'),
        keras.layers.Dense(1, activation='sigmoid')
    ])
    
    model.compile(optimizer='adam', loss=loss, metrics=['accuracy'])
    return model
