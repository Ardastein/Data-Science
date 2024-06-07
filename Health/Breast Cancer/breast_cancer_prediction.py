import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

import pandas as pd
from data_preprocessing import load_data, preprocess_data
from eda import eda
from model import train_model, evaluate_model, save_model
from visualization import plot_confusion_matrix

def main():
    file_path = 'data/breast-cancer.csv'
    df = load_data(file_path)
    print("Data Columns:", df.columns)  
    X_train, X_test, y_train, y_test = preprocess_data(df)

    eda(df)

    model = train_model(X_train, y_train)

    accuracy, report, cm = evaluate_model(model, X_test, y_test)

    plot_confusion_matrix(cm, accuracy, report)

    model_path = 'models/breast_cancer_model.pkl'
    save_model(model, model_path)

if __name__ == "__main__":
    main()
