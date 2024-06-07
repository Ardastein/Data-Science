# classification/classify.py
import sys
import os

# Add project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score
import joblib

from utils.data_loader import load_data

# Load Data
data = load_data('data/bacteria_list_200.csv')

# Print column names to debug
print("Column Names:", data.columns)

# Set 'Harmful to Humans' as the target column
target_column = 'Harmful to Humans'

if target_column in data.columns:
    X = data.drop(target_column, axis=1)
    y = data[target_column]
else:
    print(f"Error: Column '{target_column}' not found in the data.")
    sys.exit(1)

# Encode categorical features if necessary
# Assuming categorical columns need encoding. Example using pd.get_dummies
X_encoded = pd.get_dummies(X, drop_first=True)

# Preprocess Data
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Models
models = {
    'Logistic Regression': LogisticRegression(),
    'Random Forest': RandomForestClassifier(),
    'Support Vector Machine': SVC()
}

for model_name, model in models.items():
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)
    print(f"Model: {model_name}")
    print(classification_report(y_test, y_pred))
    print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
    joblib.dump(model, f'classification/models/model_{model_name.lower().replace(" ", "_")}.pkl')
