import matplotlib.pyplot as plt
import seaborn as sns

def plot_histogram(data, column):
    plt.figure(figsize=(10, 6))
    sns.histplot(data[column], kde=True)
    plt.title(f'Histogram of {column}')
    plt.show()

def plot_correlation_matrix(data):
    numeric_data = data.select_dtypes(include=['number'])
    
    plt.figure(figsize=(16, 12))  
    corr_matrix = numeric_data.corr()
    
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm', linewidths=0.5)  
    
    plt.title('Correlation Matrix')
    
    plt.xticks(rotation=45, ha='right')
    plt.yticks(rotation=0)
    
    plt.tight_layout()  
    plt.show()
