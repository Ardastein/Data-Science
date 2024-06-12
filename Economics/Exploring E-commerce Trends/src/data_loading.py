import pandas as pd

def load_data(file_path):
    """
    Load the e-commerce dataset from a CSV file.

    :param file_path: str, path to the CSV file
    :return: DataFrame, loaded dataset
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def preprocess_data(data):
    """
    Preprocess the data (e.g., handling missing values, converting data types).

    :param data: DataFrame, the dataset to preprocess
    :return: DataFrame, preprocessed dataset
    """
    data = data.dropna()  
    return data
