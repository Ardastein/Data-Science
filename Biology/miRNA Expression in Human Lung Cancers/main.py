from scripts.data_loading import load_data, preprocess_data
from scripts.data_visualization import plot_distributions, plot_correlation_heatmap, plot_class_distributions
from scripts.model_training import train_model

def main():
    file_path = "C:\\Users\\HP\\Desktop\\Missions\\Huawei\\Biology\\miRNA Expression in Human Lung Cancers\\data\\miRNA_lung.csv"
    
    data = load_data(file_path)
    preprocessed_data = preprocess_data(data)
    
    target_column = 'lineage_3'
    
    plot_distributions(preprocessed_data)
    plot_correlation_heatmap(preprocessed_data)
    plot_class_distributions(data, target_column=target_column)
    
    model = train_model(data, target_column=target_column)

if __name__ == "__main__":
    main()
