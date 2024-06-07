import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs("C:/Users/HP/Desktop/Missions/Huawei/Health/Testicular Cancer/output/figures", exist_ok=True)

data_path = 'C:/Users/HP/Desktop/Missions/Huawei/Health/Testicular Cancer/data/Testicular Cancer Dataset.csv'
df = pd.read_csv(data_path)

print("Initial Data Preview:")
print(df.head())
print("\nData Summary:")
print(df.describe())
print("\nData Info:")
print(df.info())


print("\nMissing Values:")
print(df.isnull().sum())


threshold = len(df) * 0.5
df_cleaned = df.dropna(thresh=threshold, axis=1)

numerical_cols = df_cleaned.select_dtypes(include=['float64', 'int64']).columns
for col in numerical_cols:
    median = df_cleaned[col].median()
    df_cleaned[col].fillna(median, inplace=True)

categorical_cols = df_cleaned.select_dtypes(include=['object']).columns
for col in categorical_cols:
    mode = df_cleaned[col].mode()[0]
    df_cleaned[col].fillna(mode, inplace=True)

print("\nCleaned Data Info:")
print(df_cleaned.info())

def sanitize_filename(name):
    return "".join(c if c.isalnum() else "_" for c in name)


for col in numerical_cols:
    if col in df_cleaned.columns:
        plt.figure(figsize=(10, 6))
        sns.histplot(df_cleaned[col], kde=True, bins=30)
        plt.title(f'Distribution of {col}')
        plt.xlabel(col)
        plt.ylabel('Frequency')
        sanitized_col = sanitize_filename(col)
        plt.savefig(f'C:/Users/HP/Desktop/Missions/Huawei/Health/Testicular Cancer/output/figures/distribution_{sanitized_col}.png')
        plt.close()

for col in categorical_cols:
    if col in df_cleaned.columns:
        plt.figure(figsize=(10, 6))
        sns.countplot(y=col, data=df_cleaned, palette="viridis")
        plt.title(f'Distribution of {col}')
        plt.xlabel('Count')
        plt.ylabel(col)
        sanitized_col = sanitize_filename(col)
        plt.savefig(f'C:/Users/HP/Desktop/Missions/Huawei/Health/Testicular Cancer/output/figures/distribution_{sanitized_col}.png')
        plt.close()


sns.pairplot(df_cleaned[numerical_cols])
plt.savefig('C:/Users/HP/Desktop/Missions/Huawei/Health/Testicular Cancer/output/figures/pairplot_numerical.png')
plt.close()

plt.figure(figsize=(12, 8))
correlation_matrix = df_cleaned.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix')
plt.savefig('C:/Users/HP/Desktop/Missions/Huawei/Health/Testicular Cancer/output/figures/correlation_matrix.png')
plt.close()

for cat_col in categorical_cols:
    if cat_col in df_cleaned.columns:
        for num_col in numerical_cols:
            if num_col in df_cleaned.columns:
                plt.figure(figsize=(10, 6))
                sns.boxplot(x=cat_col, y=num_col, data=df_cleaned, palette="Set2")
                plt.title(f'Boxplot of {num_col} grouped by {cat_col}')
                plt.xlabel(cat_col)
                plt.ylabel(num_col)
                sanitized_cat_col = sanitize_filename(cat_col)
                sanitized_num_col = sanitize_filename(num_col)
                plt.savefig(f'C:/Users/HP/Desktop/Missions/Huawei/Health/Testicular Cancer/output/figures/boxplot_{sanitized_num_col}_by_{sanitized_cat_col}.png')
                plt.close()

if 'Diagnosis Age' in df_cleaned.columns:
    plt.figure(figsize=(10, 6))
    sns.histplot(df_cleaned['Diagnosis Age'], kde=True, bins=30, color='blue')
    plt.title('Diagnosis Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.savefig('C:/Users/HP/Desktop/Missions/Huawei/Health/Testicular Cancer/output/figures/diagnosis_age_distribution.png')
    plt.close()

print("EDA completed and plots saved in the 'output/figures' directory.")
