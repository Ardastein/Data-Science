import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

data_path = 'C:/Users/HP/Desktop/Missions/Huawei/Food/Cheese Dataset/data/cheeses.csv'
data = pd.read_csv(data_path)

os.makedirs('results/eda_visualizations', exist_ok=True)

def perform_eda(data):
    print("Veri Setinin İlk Satırları:")
    print(data.head())

    print("\nVeri Setinin Temel İstatistikleri:")
    print(data.describe(include='all'))

    print("\nEksik Değerlerin Analizi:")
    print(data.isnull().sum())

    print("\nNumerik Değişkenlerin Dağılımı:")
    numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns
    if len(numeric_columns) > 0:
        data[numeric_columns].hist(figsize=(12, 12))
        plt.savefig("results/eda_visualizations/numeric_distribution.png")
        plt.show()
    else:
        print("Sayısal sütun bulunamadı.")

    print("\nKategorik Değişkenlerin Grafiksel Dağılımı:")
    for column in data.select_dtypes(include=['object']).columns:
        plt.figure(figsize=(10, 5))
        value_counts = data[column].value_counts()
        if len(value_counts) > 20:  # Eğer benzersiz değer sayısı çok fazlaysa, ilk 20'sini göster
            value_counts = value_counts[:20]
        sns.barplot(y=value_counts.index, x=value_counts.values, hue=value_counts.index, palette="viridis", dodge=False)
        plt.legend().set_visible(False)
        plt.title(f'{column} Dağılımı')
        plt.xlabel('Count')
        plt.ylabel(column)
        plt.yticks(rotation=0, fontsize=8)
        plt.tight_layout()
        plt.savefig(f"results/eda_visualizations/{column}_distribution.png")
        plt.show()

    if len(numeric_columns) > 0:
        print("\nKorelasyon Matrisi:")
        plt.figure(figsize=(10, 8))
        sns.heatmap(data[numeric_columns].corr(), annot=True, cmap='coolwarm', fmt=".2f")
        plt.title('Korelasyon Matrisi')
        plt.savefig("results/eda_visualizations/correlation_matrix.png")
        plt.show()

perform_eda(data)
