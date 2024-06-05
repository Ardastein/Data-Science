import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs('../visualizations', exist_ok=True)

data_path = 'data/StudentsPerformance.csv'
df = pd.read_csv(data_path)

print("First 5 rows of the dataset:")
print(df.head())

print("\nGeneral information of the dataset:")
print(df.info())

print("\nStatistical summary of the dataset:")
print(df.describe())

print("\nMissing values in the dataset:")
print(df.isnull().sum())

print("\nUnique values in each column:")
for column in df.columns:
    print(f"{column}: {df[column].nunique()}")

print("\nGender distribution:")
print(df['gender'].value_counts())

print("\nParental level of education distribution:")
print(df['parental level of education'].value_counts())

df['average score'] = df[['math score', 'reading score', 'writing score']].mean(axis=1)
print("\nSummary of average scores:")
print(df['average score'].describe())

plt.figure(figsize=(10, 6))
sns.histplot(df['average score'], bins=20, kde=True)
plt.title('Distribution of Average Scores')
plt.xlabel('Average Score')
plt.ylabel('Frequency')
plt.savefig('../visualizations/average_score_distribution.png')
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x='gender', y='math score', data=df)
plt.title('Math Score by Gender')
plt.savefig('../visualizations/math_score_by_gender.png')
plt.show()

sns.pairplot(df[['math score', 'reading score', 'writing score']])
plt.suptitle('Pairplot of Scores', y=1.02)
plt.savefig('../visualizations/pairplot_scores.png')
plt.show()

plt.figure(figsize=(12, 8))
sns.barplot(x='parental level of education', y='average score', data=df)
plt.title('Average Score by Parental Level of Education')
plt.xticks(rotation=45)
plt.savefig('../visualizations/average_score_by_parental_education.png')
plt.show()

plt.figure(figsize=(10, 6))
numeric_df = df[['math score', 'reading score', 'writing score', 'average score']]
correlation_matrix = numeric_df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix')
plt.savefig('../visualizations/correlation_matrix.png')
plt.show()

