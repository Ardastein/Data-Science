import os
import pandas as pd
from scripts.data_preprocessing import load_and_preprocess_data
from scripts.model_training import train_models, hyperparameter_tuning
from scripts.model_evaluation import evaluate_model

file_path = 'data/Heart_Disease_Prediction.csv'
df = pd.read_csv(file_path)
print("Veri setinin sütun adları:")
print(df.columns)
X_train, X_test, y_train, y_test = load_and_preprocess_data(file_path)

lr, rf, svc = train_models(X_train, y_train)

best_rf = hyperparameter_tuning(X_train, y_train)

os.makedirs('outputs/plots', exist_ok=True)
evaluate_model(lr, X_test, y_test, 'Logistic_Regression')
evaluate_model(rf, X_test, y_test, 'Random_Forest')
evaluate_model(svc, X_test, y_test, 'SVC')
evaluate_model(best_rf, X_test, y_test, 'Best_Random_Forest')
