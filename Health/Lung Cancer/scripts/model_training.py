from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

def train_model(X_train, y_train):
    """RandomForest modelini eğitir."""
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    """Modelin performansını test verisi üzerinde değerlendirir."""
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    print(f"Model Accuracy: {accuracy}")
    print(f"Classification Report:\n{report}")

def save_model(model, file_path):
    """Eğitilen modeli dosyaya kaydeder."""
    joblib.dump(model, file_path)
