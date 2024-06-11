import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import os

data_path = 'C:/Users/HP/Desktop/Missions/Huawei/Food/Cheese Dataset/data/processed_data.csv'
data = pd.read_csv(data_path)

target_column = 'country'  

X = data.drop(target_column, axis=1)  
y = data[target_column]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

os.makedirs('results/model_results', exist_ok=True)

def train_and_evaluate_model(model, model_name):
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    
    print(f"\n{model_name} Modeli İçin Değerlendirme:")
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))
    
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title(f'{model_name} Confusion Matrix')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.savefig(f"results/model_results/{model_name}_confusion_matrix.png")
    plt.show()

models = {
    'Random Forest': RandomForestClassifier(),
    'Logistic Regression': LogisticRegression(),
    'Support Vector Machine': SVC()
}

for model_name, model in models.items():
    train_and_evaluate_model(model, model_name)
