import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data_path = "data/birth.csv"

df = pd.read_csv(data_path)

print("Orijinal Sütun İsimleri:", df.columns)

df.rename(columns={
    'Deaths - Sex: ': 'Deaths_Sex',
    'Births  estimates': 'Births_estimates'
}, inplace=True)

df['Births_estimates'] = df['Births_estimates'].str.replace('.', '', regex=False)
df['Births_estimates'] = df['Births_estimates'].str.replace(',', '', regex=False).astype(float)

print("Veri Başlığı:")
print(df.head())

print("\nVeri Bilgisi:")
print(df.info())

print("\nVeri İstatistikleri:")
print(df.describe())

plt.figure(figsize=(10, 5))
sns.lineplot(x='Year', y='Births_estimates', data=df, marker='o')
plt.title('Yıllık Doğum Oranları')
plt.xlabel('Yıl')
plt.ylabel('Doğum Sayısı')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 5))
sns.lineplot(x='Year', y='Deaths_Sex', data=df, marker='o', color='r')
plt.title('Yıllık Ölüm Oranları')
plt.xlabel('Yıl')
plt.ylabel('Ölüm Sayısı')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 5))
sns.lineplot(x='Year', y='Births_estimates', data=df, marker='o', label='Doğumlar')
sns.lineplot(x='Year', y='Deaths_Sex', data=df, marker='o', color='r', label='Ölümler')
plt.title('Yıllık Doğum ve Ölüm Oranları Karşılaştırması')
plt.xlabel('Yıl')
plt.ylabel('Sayı')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 5))
sns.histplot(df['Births_estimates'], bins=30, kde=True)
plt.title('Doğum Sayılarının Dağılımı')
plt.xlabel('Doğum Sayısı')
plt.ylabel('Frekans')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 5))
sns.histplot(df['Deaths_Sex'], bins=30, kde=True, color='r')
plt.title('Ölüm Sayılarının Dağılımı')
plt.xlabel('Ölüm Sayısı')
plt.ylabel('Frekans')
plt.grid(True)
plt.show()

correlation = df['Births_estimates'].corr(df['Deaths_Sex'])
print(f"\nDoğumlar ve ölümler arasındaki korelasyon: {correlation:.2f}")

output_path = "results/"
import os

if not os.path.exists(output_path):
    os.makedirs(output_path)

plt.figure(figsize=(10, 5))
sns.lineplot(x='Year', y='Births_estimates', data=df, marker='o')
plt.title('Yıllık Doğum Oranları')
plt.xlabel('Yıl')
plt.ylabel('Doğum Sayısı')
plt.grid(True)
plt.savefig(os.path.join(output_path, 'yearly_births.png'))

plt.figure(figsize=(10, 5))
sns.lineplot(x='Year', y='Deaths_Sex', data=df, marker='o', color='r')
plt.title('Yıllık Ölüm Oranları')
plt.xlabel('Yıl')
plt.ylabel('Ölüm Sayısı')
plt.grid(True)
plt.savefig(os.path.join(output_path, 'yearly_deaths.png'))

plt.figure(figsize=(10, 5))
sns.lineplot(x='Year', y='Births_estimates', data=df, marker='o', label='Doğumlar')
sns.lineplot(x='Year', y='Deaths_Sex', data=df, marker='o', color='r', label='Ölümler')
plt.title('Yıllık Doğum ve Ölüm Oranları Karşılaştırması')
plt.xlabel('Yıl')
plt.ylabel('Sayı')
plt.legend()
plt.grid(True)
plt.savefig(os.path.join(output_path, 'births_vs_deaths.png'))

print("Analiz tamamlandı ve grafikler kaydedildi.")
