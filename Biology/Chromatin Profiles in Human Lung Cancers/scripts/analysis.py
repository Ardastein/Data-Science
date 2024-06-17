import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

results_dir = 'results'
if not os.path.exists(results_dir):
    os.makedirs(results_dir)

data_path = 'data/lung_chromatin.csv'
df = pd.read_csv(data_path)

print("Data Info:")
print(df.info())

print("\nData Description:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns

selected_cols = numerical_cols[:5]  
for col in selected_cols:
    plt.figure(figsize=(10, 6))
    sns.histplot(df[col].dropna(), kde=True)
    plt.title(f'Distribution of {col}')
    plt.savefig(os.path.join(results_dir, f'distribution_{col}.png'))
    plt.close()
    print(f"Saved distribution plot for {col}")

sns.pairplot(df[selected_cols].dropna(), diag_kind='kde')
plt.title('Pairplot of Selected Features')
plt.savefig(os.path.join(results_dir, 'pairplot.png'))
plt.close()
print("Saved pairplot")


plt.figure(figsize=(12, 10))

correlation_matrix = df[numerical_cols].corr().round(2)
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', annot_kws={"size": 8})
plt.title('Correlation Matrix')
plt.savefig(os.path.join(results_dir, 'correlation_matrix.png'))
plt.close()
print("Saved correlation matrix")

if 'lineage_1' in df.columns and df['lineage_1'].nunique() < 50 and df['lineage_1'].isna().sum() < df.shape[0] // 2:
    categorical_col = 'lineage_1'
else:
    for col in df.select_dtypes(include=['object']).columns:
        if df[col].nunique() < 50 and df[col].isna().sum() < df.shape[0] // 2:
            categorical_col = col
            break

if categorical_col:
    print(f"Using {categorical_col} as the categorical column for boxplot.")
    feature_for_boxplot = selected_cols[0]  
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=categorical_col, y=feature_for_boxplot, data=df.dropna(subset=[feature_for_boxplot, categorical_col]))
    plt.title(f'Boxplot of {feature_for_boxplot} by {categorical_col}')
    plt.savefig(os.path.join(results_dir, f'boxplot_{feature_for_boxplot}_by_{categorical_col}.png'))
    plt.close()
    print(f"Saved boxplot for {feature_for_boxplot} by {categorical_col}")

print(f"All selected visualizations saved in the {results_dir} directory.")
