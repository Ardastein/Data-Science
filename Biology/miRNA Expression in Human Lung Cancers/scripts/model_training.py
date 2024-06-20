import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

def preprocess_data(data, target_column):
    numeric_data = data.select_dtypes(include=['float64', 'int64'])
    
    numeric_data = numeric_data.dropna(axis=1, how='all')
    
    imputer = SimpleImputer(strategy='mean')
    numeric_data_imputed = pd.DataFrame(imputer.fit_transform(numeric_data), columns=numeric_data.columns)

    numeric_data_imputed[target_column] = data[target_column]

    return numeric_data_imputed

def train_model(data, target_column):
    preprocessed_data = preprocess_data(data, target_column)
    
    X = preprocessed_data.drop(target_column, axis=1)
    y = preprocessed_data[target_column]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred, zero_division=1))

    return model

if __name__ == "__main__":
    file_path = "C:\\Users\\HP\\Desktop\\Missions\\Huawei\\Biology\\miRNA Expression in Human Lung Cancers\\data\\miRNA_lung.csv"
    data = pd.read_csv(file_path)
    model = train_model(data, target_column='lineage_3')  
