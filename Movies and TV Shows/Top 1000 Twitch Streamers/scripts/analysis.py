import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

if not os.path.exists('outputs'):
    os.mkdir('outputs')

if not os.path.exists('outputs/figures'):
    os.mkdir('outputs/figures')

data_path = 'data/dataset.csv'
df = pd.read_csv(data_path)

print("Veri Seti Sütunları:")
print(df.columns)

print("Veri Seti İlk 5 Satır:")
print(df.head())

print("\nVeri Seti Bilgisi:")
print(df.info())

print("\nEksik Veri Kontrolü:")
print(df.isnull().sum())

df = df.dropna()

print("\nTemizlenmiş Veri Seti İlk 5 Satır:")
print(df.head())

plt.figure(figsize=(20, 16))
sns.countplot(y='MOST_STREAMED_GAME', data=df, order=df['MOST_STREAMED_GAME'].value_counts().index)
plt.title('Oynanan Oyunların Dağılımı')
plt.xlabel('Oyun Sayısı')
plt.ylabel('Oyun')
plt.tight_layout()
plt.savefig('outputs/figures/most_streamed_game_distribution.png')
plt.close()

plt.figure(figsize=(10, 6))
sns.histplot(df['AVG_VIEWERS_PER_STREAM'], bins=30, kde=True)
plt.title('Ortalama İzleyici Sayısı Dağılımı')
plt.xlabel('Ortalama İzleyici Sayısı')
plt.ylabel('Frekans')
plt.tight_layout()
plt.savefig('outputs/figures/average_viewers_distribution.png')
plt.close()

plt.figure(figsize=(10, 6))
sns.scatterplot(x='AVG_VIEWERS_PER_STREAM', y='TOTAL_FOLLOWERS', data=df)
plt.title('İzleyici Sayısı vs Abone Sayısı')
plt.xlabel('Ortalama İzleyici Sayısı')
plt.ylabel('Abone Sayısı')
plt.tight_layout()
plt.savefig('outputs/figures/viewers_vs_followers.png')
plt.close()

plt.figure(figsize=(10, 6))
sns.histplot(df['TOTAL_TIME_STREAMED'], bins=30, kde=True)
plt.title('Toplam Yayın Süresi Dağılımı')
plt.xlabel('Toplam Yayın Süresi (saat)')
plt.ylabel('Frekans')
plt.tight_layout()
plt.savefig('outputs/figures/total_time_streamed_distribution.png')
plt.close()

plt.figure(figsize=(10, 6))
sns.boxplot(x='TYPE', y='AVG_VIEWERS_PER_STREAM', data=df)
plt.title('Kategorilere Göre İzleyici Sayıları')
plt.xlabel('Kategori')
plt.ylabel('Ortalama İzleyici Sayısı')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('outputs/figures/viewers_by_category.png')
plt.close()

top_streamers = df.sort_values(by='TOTAL_FOLLOWERS', ascending=False).head(10)
plt.figure(figsize=(10, 6))
sns.barplot(y='NAME', x='TOTAL_FOLLOWERS', data=top_streamers)
plt.title('En Popüler 10 Streamer')
plt.xlabel('Takipçi Sayısı')
plt.ylabel('Streamer Adı')
plt.tight_layout()
plt.savefig('outputs/figures/top_10_streamers.png')
plt.close()

print("Grafikler 'outputs/figures' klasörüne kaydedildi.")
