import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.metrics import mean_squared_error
import utils.data_preprocessing as dp

def build_ann_model(input_shape):
    model = Sequential()
    model.add(Dense(64, input_dim=input_shape, activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(1, activation='linear'))
    
    model.compile(optimizer='adam', loss='mse', metrics=['mae'])
    return model

if __name__ == "__main__":
    data_path = 'data/abalone1.data'
    data = dp.load_data(data_path)
    X_train, X_test, y_train, y_test = dp.preprocess_data(data)
    
    model = build_ann_model(X_train.shape[1])
    model.summary()
    
    model.fit(X_train, y_train, epochs=50, batch_size=10, validation_split=0.2)
    
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    print(f'Mean Squared Error: {mse}')
