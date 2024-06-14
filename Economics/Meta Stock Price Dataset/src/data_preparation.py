import pandas as pd
import numpy as np

def load_and_prepare_data(file_path):
    df = pd.read_csv(file_path)
    
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    
    df = df.fillna(method='ffill')
    
    return df

if __name__ == "__main__":
    file_path = 'data/Meta.csv'
    df = load_and_prepare_data(file_path)
    print(df.head())
