import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data_path = 'data/xAPI-Edu-Data.csv'
df = pd.read_csv(data_path)

print(df.info())

print(df.head())

print(df.isnull().sum())

print(df.describe())

numeric_features = df.select_dtypes(include=[np.number]).columns.tolist()
df[numeric_features].hist(bins=15, figsize=(15, 10), layout=(3, 3))

numeric_df = df[numeric_features]
corr_matrix = numeric_df.corr()
plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')

categorical_features = df.select_dtypes(include=[object]).columns.tolist()

plt.figure(figsize=(20, 15))
for i, feature in enumerate(categorical_features, 1):
    plt.subplot(5, 3, i)
    sns.countplot(data=df, x=feature)
    plt.title(f'Count Plot of {feature}')
    plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
