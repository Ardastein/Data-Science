import pandas as pd
import numpy as np

def load_data(file_path):
    return pd.read_csv(file_path)

def preprocess_data(df):
    df = df.dropna()
    df = pd.get_dummies(df, drop_first=True)
    return df

if __name__ == "__main__":
    data_path = "data/Mental Health Dataset.csv"
    df = load_data(data_path)
    df = preprocess_data(df)
    df.to_csv("data/preprocessed_data.csv", index=False)
    print("Data preprocessing completed and saved to preprocessed_data.csv")