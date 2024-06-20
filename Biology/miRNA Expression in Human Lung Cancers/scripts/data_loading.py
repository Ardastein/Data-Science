import pandas as pd

def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

def preprocess_data(data):
    numeric_data = data.select_dtypes(include=['float64', 'int64'])
    return numeric_data

if __name__ == "__main__":
    file_path = "C:\\Users\\HP\\Desktop\\Missions\\Huawei\\Biology\\miRNA Expression in Human Lung Cancers\\data\\miRNA_lung.csv"
    data = load_data(file_path)
    preprocessed_data = preprocess_data(data)
    print(preprocessed_data.head())
