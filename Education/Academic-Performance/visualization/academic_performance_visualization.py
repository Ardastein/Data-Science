import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data_path = 'data/xAPI-Edu-Data.csv'
df = pd.read_csv(data_path)

plt.figure(figsize=(10, 6))
sns.countplot(x='Class', data=df)
plt.title('Distribution of Final Grades')
plt.xlabel('Final Grade')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(x='Class', hue='gender', data=df)
plt.title('Gender vs Final Grade')
plt.xlabel('Final Grade')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(12, 8))
sns.countplot(x='Class', hue='NationalITy', data=df)
plt.title('Nationality vs Final Grade')
plt.xlabel('Final Grade')
plt.ylabel('Count')
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1))
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(x='Class', hue='Relation', data=df)
plt.title('Relation vs Final Grade')
plt.xlabel('Final Grade')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(12, 8))
sns.countplot(x='Class', hue='ParentAnsweringSurvey', data=df)
plt.title('Parent\'s Educational Level vs Final Grade')
plt.xlabel('Final Grade')
plt.ylabel('Count')
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1))
plt.show()

numeric_features = df.select_dtypes(include=['int64', 'float64']).columns.tolist()

plt.figure(figsize=(20, 15))
for i, feature in enumerate(numeric_features, 1):
    plt.subplot(5, 3, i)
    sns.boxplot(x='Class', y=feature, data=df)
    plt.title(f'{feature} vs Final Grade')
    plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
