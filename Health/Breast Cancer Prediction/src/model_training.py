import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from src.data_utils import load_and_prepare_data  
def train_model(file_path):
    data = load_and_prepare_data(file_path)
    
    X = data.drop('Class', axis=1)
    y = data['Class']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    
    print("Doğruluk Skoru:", accuracy_score(y_test, y_pred))
    print("\nSınıflandırma Raporu:\n", classification_report(y_test, y_pred))
    print("\nKarmaşıklık Matrisi:\n", confusion_matrix(y_test, y_pred))

if __name__ == "__main__":
    file_path = "C:/Users/HP/Desktop/Missions/Huawei/Health/Breast Cancer Prediction/data/Breast Cancer Prediction.csv"
    train_model(file_path)
