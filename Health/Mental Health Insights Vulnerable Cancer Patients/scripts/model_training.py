import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, classification_report

def load_data(file_path):
    return pd.read_csv(file_path)

def train_model(df):
    print("Inspecting data types:")
    print(df.dtypes)
    
    target_column = 'predicted_neutral'  
    X = df.drop(target_column, axis=1)
    y = df[target_column]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print("Data split into training and test sets.")
    print(f"Training data shape: {X_train.shape}, Test data shape: {X_test.shape}")
    
    model = XGBClassifier(n_estimators=10, max_depth=3, use_label_encoder=False, eval_metric='logloss')
    
    print("Starting model training...")
    model.fit(X_train, y_train)
    print("Model training completed.")
    
    y_pred = model.predict(X_test)
    
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    
    print(f'Accuracy: {accuracy}')
    print(f'Classification Report: \n{report}')
    
    return model

if __name__ == "__main__":
    data_path = "data/preprocessed_data.csv"
    df = load_data(data_path)
    print("Data loaded successfully. Shape:", df.shape)
    model = train_model(df)    
    print("Model training script completed.")
