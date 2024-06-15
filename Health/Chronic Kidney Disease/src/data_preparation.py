import pandas as pd

def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

def clean_data(data):
    numeric_columns = data.select_dtypes(include=['number']).columns
    
    data[numeric_columns] = data[numeric_columns].fillna(data[numeric_columns].median())
    
    for column in data.select_dtypes(include=['object']).columns:
        data[column] = data[column].fillna(data[column].mode()[0])
    
    return data