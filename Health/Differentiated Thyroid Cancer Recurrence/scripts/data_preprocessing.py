import pandas as pd

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

def initial_exploration(df):
    print("Data Info:")
    print(df.info())
    print("\nDescriptive Statistics:")
    print(df.describe())
    print("\nMissing Values:")
    print(df.isnull().sum())

if __name__ == "__main__":
    file_path = "C:/Users/HP/Desktop/Missions/Huawei/Health/Differentiated Thyroid Cancer Recurrence/data/Thyroid_Diff.csv"
    df = load_data(file_path)
    initial_exploration(df)
