import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data_path = 'data/Cancer_Data.csv'
df = pd.read_csv(data_path)

df.drop(columns=['Unnamed: 32'], inplace=True)

df.drop(columns=['id'], inplace=True)

df['diagnosis'] = df['diagnosis'].map({'M': 1, 'B': 0})

print("Veri Kümesinin İlk 5 Satırı:")
print(df.head())

print("\nVeri Kümesi Bilgileri:")
print(df.info())

print("\nEksik Değerlerin Sayısı:")
print(df.isnull().sum())

df.fillna(df.mean(), inplace=True)

print("\nEksik Değerlerin Doldurulmasından Sonra:")
print(df.isnull().sum())

clean_data_path = 'data/Cleaned_Cancer_Data.csv'
df.to_csv(clean_data_path, index=False)

print(f"Temizlenmiş veri kaydedildi: {clean_data_path}")
