import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_distributions(data, num_bins=20, top_n=5, save_path="data"):
    numeric_data = data.select_dtypes(include=['float64', 'int64'])
    top_columns = numeric_data.var().nlargest(top_n).index
    selected_data = numeric_data[top_columns]
    
    selected_data.hist(bins=num_bins, figsize=(20, 15), edgecolor='black', grid=False)
    plt.suptitle('Top {} Feature Distributions'.format(top_n), fontsize=20)
    plt.savefig(os.path.join(save_path, 'feature_distributions.png'))
    plt.show()

def plot_correlation_heatmap(data, save_path="data"):
    numeric_data = data.select_dtypes(include=['float64', 'int64'])
    corr_matrix = numeric_data.corr()

    plt.figure(figsize=(12, 8))
    sns.heatmap(corr_matrix, annot=False, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title('Correlation Heatmap', fontsize=18)
    plt.savefig(os.path.join(save_path, 'correlation_heatmap.png'))
    plt.show()

def plot_class_distributions(data, target_column, save_path="data"):
    plt.figure(figsize=(10, 6))
    sns.countplot(y=target_column, data=data, hue=target_column, palette='viridis', legend=False)
    plt.title('Class Distribution', fontsize=18)
    plt.xlabel('Count', fontsize=14)
    plt.ylabel(target_column, fontsize=14)
    plt.savefig(os.path.join(save_path, 'class_distribution.png'))
    plt.show()

if __name__ == "__main__":
    file_path = "C:\\Users\\HP\\Desktop\\Missions\\Huawei\\Biology\\miRNA Expression in Human Lung Cancers\\data\\miRNA_lung.csv"
    save_path = "C:\\Users\\HP\\Desktop\\Missions\\Huawei\\Biology\\miRNA Expression in Human Lung Cancers\\data"
    
    data = pd.read_csv(file_path)
    target_column = 'lineage_3'
    
    plot_distributions(data, top_n=5, save_path=save_path)  
    plot_correlation_heatmap(data, save_path=save_path)
    plot_class_distributions(data, target_column=target_column, save_path=save_path)
