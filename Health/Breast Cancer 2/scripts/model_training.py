import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
import joblib

data_path = 'data/Cleaned_Cancer_Data.csv'
df = pd.read_csv(data_path)

print("\nEksik Değerlerin Sayısı:")
print(df.isnull().sum().sum())

if df.isnull().sum().sum() > 0:
    raise ValueError("Veride hala eksik değerler var. Lütfen data_preparation.py dosyasını çalıştırarak eksik değerleri doldurun.")

X = df.drop('diagnosis', axis=1)  
y = df['diagnosis']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_scaled, y_train)

svm = SVC(kernel='linear')
svm.fit(X_train_scaled, y_train)

knn_predictions = knn.predict(X_test_scaled)
svm_predictions = svm.predict(X_test_scaled)

print("KNN Sınıflandırma Raporu:")
print(classification_report(y_test, knn_predictions))

print("\nSVM Sınıflandırma Raporu:")
print(classification_report(y_test, svm_predictions))

joblib.dump(knn, 'results/models/knn_model.joblib')
joblib.dump(svm, 'results/models/svm_model.joblib')
joblib.dump(scaler, 'results/models/scaler.joblib')

print("Modeller kaydedildi.")
