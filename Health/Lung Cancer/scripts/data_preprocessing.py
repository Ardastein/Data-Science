import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

def load_data(file_path):
    """Veri setini yükler."""
    data = pd.read_csv(file_path)
    return data


def preprocess_data(data):
    """Veriyi temizler, dönüştürür ve eğitim/test setlerine böler."""
    data = data.dropna()  
    
    label_encoder = LabelEncoder()
    data['LUNG_CANCER'] = label_encoder.fit_transform(data['LUNG_CANCER'])
    
    X = data.drop('LUNG_CANCER', axis=1)
    y = data['LUNG_CANCER']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    
    return X_train, X_test, y_train, y_test, scaler