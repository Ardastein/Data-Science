import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import os

cleaned_data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data'))
train = pd.read_csv(os.path.join(cleaned_data_path, 'cleaned_train.csv'))

X = train.drop('Weekly_Sales', axis=1)
y = train['Weekly_Sales']

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_val)
print(f"Mean Absolute Error: {mean_absolute_error(y_val, y_pred)}")
print(f"Mean Squared Error: {mean_squared_error(y_val, y_pred)}")
print(f"R2 Score: {r2_score(y_val, y_pred)}")

import joblib
output_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../output'))
joblib.dump(model, os.path.join(output_path, 'sales_forecasting_model.pkl'))
