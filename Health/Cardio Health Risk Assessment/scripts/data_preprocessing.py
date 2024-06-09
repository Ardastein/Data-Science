import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_and_preprocess_data(file_path):
    df = pd.read_csv(file_path)
    
    categorical_columns = ['Sex', 'Chest pain type', 'FBS over 120', 'EKG results', 
                           'Exercise angina', 'Slope of ST', 'Number of vessels fluro', 'Thallium']
    
    df = pd.get_dummies(df, columns=categorical_columns, drop_first=True)
    
    numeric_columns = df.select_dtypes(include=['number']).columns
    df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())
    
    target_column = 'Heart Disease'
    
    df[target_column] = df[target_column].map({'Absence': 0, 'Presence': 1})
    
    X = df.drop(columns=[target_column])
    y = df[target_column]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    return X_train_scaled, X_test_scaled, y_train, y_test
