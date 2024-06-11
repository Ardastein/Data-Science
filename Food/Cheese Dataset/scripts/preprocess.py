import pandas as pd

data_path = 'C:/Users/HP/Desktop/Missions/Huawei/Food/Cheese Dataset/data/cheeses.csv'
data = pd.read_csv(data_path)

def preprocess_data(data):
    for column in data.select_dtypes(include=['float64', 'int64']).columns:
        data[column].fillna(data[column].median(), inplace=True)

    for column in data.select_dtypes(include=['object']).columns:
        data[column] = data[column].astype('category').cat.codes

    processed_data_path = 'C:/Users/HP/Desktop/Missions/Huawei/Food/Cheese Dataset/data/processed_data.csv'
    data.to_csv(processed_data_path, index=False)

    print("Veri ön işleme tamamlandı ve işlenmiş veri kaydedildi.")

preprocess_data(data)
