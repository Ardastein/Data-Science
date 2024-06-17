import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

def load_data(file_path):
    column_names = ['Sex', 'Length', 'Diameter', 'Height', 'Whole_weight',
                    'Shucked_weight', 'Viscera_weight', 'Shell_weight', 'Rings']
    data = pd.read_csv(file_path, names=column_names)
    return data

def preprocess_data(data):
    data = data.dropna()
    data['Sex'] = data['Sex'].map({'M': 0, 'F': 1, 'I': 2})
    features = data.drop('Rings', axis=1)
    labels = data['Rings']
    
    scaler = StandardScaler()
    features = scaler.fit_transform(features)
    
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)
    
    return X_train, X_test, y_train, y_test
