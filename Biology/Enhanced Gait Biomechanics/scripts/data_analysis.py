import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

data_path = r"C:\Users\HP\Desktop\Missions\Huawei\Biology\Enhanced Gait Biomechanics\data\Gait.csv"

df = pd.read_csv(data_path)

print("Veri Hakkında Genel Bilgi:")
print(df.info())
print("\n")

print("Verinin İlk 5 Satırı:")
print(df.head())
print("\n")

print("Verinin Temel İstatistikleri:")
print(df.describe())
print("\n")

output_path = os.path.join(os.path.dirname(data_path), 'results')
os.makedirs(output_path, exist_ok=True)

print("Grafik 1: Histogramlar oluşturuluyor...")
plt.figure(figsize=(10, 6))
df.hist(bins=30, figsize=(20, 15))
plt.suptitle('Histogram of All Columns', fontsize=16)
plt.savefig(os.path.join(output_path, 'histograms.png'))
plt.close()
print("Grafik 1: Histogramlar kaydedildi.\n")

print("Grafik 2: Pairplot oluşturuluyor...")
plt.figure(figsize=(10, 6))
sns.pairplot(df.sample(n=1000))  
plt.suptitle('Pairplot of All Columns', fontsize=16)
plt.savefig(os.path.join(output_path, 'pairplot.png'))
plt.close()
print("Grafik 2: Pairplot kaydedildi.\n")

print("Grafik 3: Isı haritası oluşturuluyor...")
plt.figure(figsize=(12, 8))
corr = df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap', fontsize=16)
plt.savefig(os.path.join(output_path, 'heatmap.png'))
plt.close()
print("Grafik 3: Isı haritası kaydedildi.\n")

print("Grafik 4: Boxplotlar oluşturuluyor...")
plt.figure(figsize=(12, 8))
df.plot(kind='box', subplots=True, layout=(int(len(df.columns) / 3) + 1, 3), figsize=(20, 10), sharex=False, sharey=False)
plt.suptitle('Boxplot of All Columns', fontsize=16)
plt.savefig(os.path.join(output_path, 'boxplots.png'))
plt.close()
print("Grafik 4: Boxplotlar kaydedildi.\n")

print("Grafik 5: Ortalama değerler bar grafiği oluşturuluyor...")
plt.figure(figsize=(12, 8))
df.mean().plot(kind='bar')
plt.title('Mean Value of Each Column', fontsize=16)
plt.savefig(os.path.join(output_path, 'mean_barplot.png'))
plt.close()
print("Grafik 5: Ortalama değerler bar grafiği kaydedildi.\n")

print("Grafik 6: Scatter matrix oluşturuluyor...")
plt.figure(figsize=(12, 8))
pd.plotting.scatter_matrix(df.sample(n=1000), alpha=0.2, figsize=(20, 15), diagonal='kde')  
plt.suptitle('Scatter Matrix of All Columns', fontsize=16)
plt.savefig(os.path.join(output_path, 'scatter_matrix.png'))
plt.close()
print("Grafik 6: Scatter matrix kaydedildi.\n")

print(f"Tüm grafikler '{output_path}' klasörüne kaydedildi.")
