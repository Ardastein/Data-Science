import pandas as pd
from scripts.data_preprocessing import load_data, preprocess_data
from scripts.visualization import plot_distributions, plot_correlation_heatmap, plot_count
from scripts.model_training import train_model, evaluate_model, save_model

file_path = 'data/survey lung cancer.csv'

data = load_data(file_path)
print("Veri Başarıyla Yüklendi. İlk 5 Satır:\n", data.head())

data.columns = [col.upper().replace(' ', '_') for col in data.columns]
print("Düzenlenmiş Veri Sütun İsimleri:\n", data.columns)

print("Veri Dağılımı:")
plot_distributions(data)

print("Korelasyon Isı Haritası:")
plot_correlation_heatmap(data)

print("Kategori Dağılımları:")
for column in data.columns:
    plot_count(data, column)

X_train, X_test, y_train, y_test, scaler = preprocess_data(data)
print("Veri Başarıyla Ön İşlendi.")

model = train_model(X_train, y_train)
print("Model Başarıyla Eğitildi.")

evaluate_model(model, X_test, y_test)

model_file_path = 'models/trained_model.pkl'
save_model(model, model_file_path)
print(f"Model Başarıyla '{model_file_path}' Yoluna Kaydedildi.")
