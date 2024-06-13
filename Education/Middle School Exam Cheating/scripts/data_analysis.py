import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

data_path = "data/middle school english exam - Feuille 1.csv"

df = pd.read_csv(data_path)

def create_folders():
    os.makedirs("results/visuals", exist_ok=True)

create_folders()

print("Veri Özeti:")
print(df.info())

print("\nİlk 5 Satır:")
print(df.head())

print("\nEksik Veriler:")
print(df.isnull().sum())

print("\nBetimsel İstatistikler:")
print(df.describe())


plt.figure(figsize=(10, 6))
sns.histplot(df['test_1'], kde=True, bins=20, label='Test 1', color='blue')
sns.histplot(df['test_2'].dropna(), kde=True, bins=20, label='Test 2', color='orange')
plt.title('Test Puanlarının Dağılımı')
plt.xlabel('Test Puanı')
plt.ylabel('Frekans')
plt.legend()
plt.savefig('results/visuals/test_score_distribution.png')
plt.close()

plt.figure(figsize=(10, 6))
sns.boxplot(x='sex', y='test_1', data=df)
plt.title('Cinsiyete Göre Test 1 Puanları')
plt.xlabel('Cinsiyet')
plt.ylabel('Test 1 Puanı')
plt.savefig('results/visuals/test_1_scores_by_gender.png')
plt.close()

plt.figure(figsize=(10, 6))
sns.boxplot(x='sex', y='test_2', data=df)
plt.title('Cinsiyete Göre Test 2 Puanları')
plt.xlabel('Cinsiyet')
plt.ylabel('Test 2 Puanı')
plt.savefig('results/visuals/test_2_scores_by_gender.png')
plt.close()


df['age'] = 2021 - pd.to_datetime(df['date_of_birth']).dt.year

plt.figure(figsize=(10, 6))
sns.scatterplot(x='age', y='test_1', data=df, hue='sex', alpha=0.7)
plt.title('Yaşa Göre Test 1 Puanları')
plt.xlabel('Yaş')
plt.ylabel('Test 1 Puanı')
plt.savefig('results/visuals/test_1_scores_by_age.png')
plt.close()

plt.figure(figsize=(10, 6))
sns.scatterplot(x='age', y='test_2', data=df, hue='sex', alpha=0.7)
plt.title('Yaşa Göre Test 2 Puanları')
plt.xlabel('Yaş')
plt.ylabel('Test 2 Puanı')
plt.savefig('results/visuals/test_2_scores_by_age.png')
plt.close()

plt.figure(figsize=(10, 6))
sns.kdeplot(df['test_1'], shade=True)
plt.title('Test 1 Puanlarının Yoğunluğu')
plt.xlabel('Test 1 Puanı')
plt.ylabel('Yoğunluk')
plt.savefig('results/visuals/test_1_score_density.png')
plt.close()

plt.figure(figsize=(10, 6))
sns.boxplot(x='cheated', y='test_1', data=df)
plt.title('Kopya Çekmeye Göre Test 1 Puanları')
plt.xlabel('Kopya Çekme Durumu')
plt.ylabel('Test 1 Puanı')
plt.savefig('results/visuals/test_1_scores_by_cheating.png')
plt.close()

plt.figure(figsize=(10, 6))
sns.boxplot(x='cheated', y='test_2', data=df)
plt.title('Kopya Çekmeye Göre Test 2 Puanları')
plt.xlabel('Kopya Çekme Durumu')
plt.ylabel('Test 2 Puanı')
plt.savefig('results/visuals/test_2_scores_by_cheating.png')
plt.close()

print("Grafikler oluşturuldu ve results/visuals/ klasörüne kaydedildi.")
