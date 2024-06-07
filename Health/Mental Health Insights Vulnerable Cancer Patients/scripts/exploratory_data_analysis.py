import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    return pd.read_csv(file_path)

def plot_distribution(df, column, output_path):
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x=column)
    plt.title(f'Distribution of {column}')
    plt.savefig(output_path)
    plt.show()

def plot_correlation_heatmap(df, output_path):
    plt.figure(figsize=(12, 10))
    correlation_matrix = df.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Heatmap')
    plt.savefig(output_path)
    plt.show()

if __name__ == "__main__":
    data_path = "data/preprocessed_data.csv"
    df = load_data(data_path)
    
    print("Column names in the dataset:", df.columns)
    
    plot_distribution(df, 'predicted_neutral', 'results/eda_visualizations/predicted_neutral_distribution.png')
    
    plot_correlation_heatmap(df, 'results/eda_visualizations/correlation_heatmap.png')
    
    print("EDA completed and visualizations saved to results/eda_visualizations/")
