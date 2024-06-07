import pandas as pd

def load_and_prepare_data(file_path):
    data = pd.read_csv(file_path)
    
    print("Veri setinin ilk beş satırı:")
    print(data.head())

    missing_values = data.isnull().sum()
    print("\nEksik değerler:")
    print(missing_values)

    data = data.fillna(data.mean())

    return data

if __name__ == "__main__":
    file_path = "C:/Users/HP/Desktop/Missions/Huawei/Health/Breast Cancer Prediction/data/Breast Cancer Prediction.csv"
    data = load_and_prepare_data(file_path)
    print("\nVeri hazırlama tamamlandı.")
