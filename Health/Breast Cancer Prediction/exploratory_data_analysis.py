import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/src")

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src.data_utils import load_and_prepare_data  

file_path = "C:/Users/HP/Desktop/Missions/Huawei/Health/Breast Cancer Prediction/data/Breast Cancer Prediction.csv"
data = load_and_prepare_data(file_path)

print("Temel istatistikler:")
print(data.describe())

plt.figure(figsize=(8, 6))
sns.countplot(x='Class', data=data)
plt.title('Sınıf Dağılımı')
plt.xlabel('Sınıf')
plt.ylabel('Frekans')
plt.show()

plt.figure(figsize=(12, 10))
correlation_matrix = data.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Özelliklerin Korelasyon Matrisi')
plt.show()

plt.figure(figsize=(8, 6))
sns.boxplot(x='Class', y='Clump Thickness', data=data)
plt.title('Clump Thickness ve Sınıf Dağılımı')
plt.xlabel('Sınıf')
plt.ylabel('Clump Thickness')
plt.show()
