import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src.data_utils import load_and_prepare_data  

def create_visualizations(file_path):
    data = load_and_prepare_data(file_path)
    
    plt.figure(figsize=(8, 6))
    sns.countplot(x='Class', data=data)
    plt.title('Sınıf Dağılımı')
    plt.xlabel('Sınıf')
    plt.ylabel('Frekans')
    plt.show()

    data.hist(bins=30, figsize=(20, 15))
    plt.suptitle('Özelliklerin Histogramları')
    plt.show()

    sns.pairplot(data, hue='Class')
    plt.title('Pairplot')
    plt.show()

    plt.figure(figsize=(12, 10))
    sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
    plt.title('Korelasyon Matrisi')
    plt.show()

if __name__ == "__main__":
    file_path = "C:/Users/HP/Desktop/Missions/Huawei/Health/Breast Cancer Prediction/data/Breast Cancer Prediction.csv"
    create_visualizations(file_path)
