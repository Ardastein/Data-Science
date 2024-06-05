import pandas as pd

def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

def clean_data(data):
    data = data.drop_duplicates()
    data = data.fillna(method='ffill')
    return data

if __name__ == "__main__":
    file_path = "data/College_data.csv"
    data = load_data(file_path)
    clean_data = clean_data(data)
    clean_data.to_csv("data/Cleaned_Top_Indian_Colleges.csv", index=False)
