import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data_path = 'data/Cleaned_Cancer_Data.csv'
df = pd.read_csv(data_path)

if df.isnull().sum().sum() > 0:
    raise ValueError("Veride eksik değerler var. Lütfen data_preparation.py dosyasını çalıştırarak eksik değerleri doldurun.")

output_dir = 'results/charts/'

def plot_distribution(column_name):
    plt.figure(figsize=(10, 6))
    sns.histplot(df[column_name], kde=True, bins=30)
    plt.title(f'Distribution of {column_name}')
    plt.savefig(f"{output_dir}{column_name}_distribution.png")
    plt.close()

def plot_pairplot():
    plt.figure(figsize=(10, 6))
    sns.pairplot(df, hue='diagnosis')  
    plt.savefig(f"{output_dir}pairplot.png")
    plt.close()

def plot_correlation():
    plt.figure(figsize=(12, 10))
    correlation_matrix = df.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.savefig(f"{output_dir}correlation_matrix.png")
    plt.close()

for column in df.columns:
    if df[column].dtype in ['int64', 'float64'] and column != 'diagnosis':
        plot_distribution(column)

plot_pairplot()
plot_correlation()

print("Grafikler oluşturuldu ve kaydedildi.")
