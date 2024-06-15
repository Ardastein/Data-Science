import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.data_preparation import load_data, clean_data
from src.data_analysis import basic_statistics, value_counts
from src.data_visualization import plot_histogram, plot_correlation_matrix
from models.model_training import train_model

def main():
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'kidney.csv'))
    data = load_data(file_path)
    data = clean_data(data)
    
    print("Sütun İsimleri:", data.columns)
    
    print(basic_statistics(data))
    
    print(value_counts(data, 'Diagnosis'))
    
    plot_histogram(data, 'Age')
    
    plot_correlation_matrix(data)
    
    model = train_model(data, 'Diagnosis')

if __name__ == "__main__":
    main()