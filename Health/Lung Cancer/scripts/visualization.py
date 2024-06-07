import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_distributions(data):
    """Veri setindeki değişkenlerin dağılımını görselleştirir."""
    sns.pairplot(data, hue='LUNG_CANCER')
    plt.show()

def plot_correlation_heatmap(data):
    """Değişkenler arasındaki korelasyonu ısı haritası ile gösterir."""
    numeric_data = data.select_dtypes(include=['float64', 'int64'])
    plt.figure(figsize=(12, 8))
    correlation = numeric_data.corr()
    sns.heatmap(correlation, annot=True, cmap='coolwarm')
    plt.show()

def plot_count(data, column):
    """Belirli bir sütunun kategorik dağılımını gösterir."""
    sns.countplot(data[column])
    plt.show()
