# eda/eda.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno

# Use the Agg backend for rendering
import matplotlib
matplotlib.use('Agg')

# Load the dataset
data_path = 'data/Kaggle_Datasets.csv'
df = pd.read_csv(data_path)

# Display basic information
print("Basic Information:")
print(df.info())
print("\n")

# Display basic statistics
print("Basic Statistics:")
print(df.describe())
print("\n")

# Check for missing values
print("Missing Values:")
print(df.isnull().sum())
print("\n")

# Visualize missing values
print("Visualizing missing values...")
try:
    msno.matrix(df)
    plt.savefig('visualization/missing_values_matrix.png')
    plt.close()

    msno.heatmap(df)
    plt.savefig('visualization/missing_values_heatmap.png')
    plt.close()
    print("Missing values visualization saved.\n")
except Exception as e:
    print(f"Error visualizing missing values: {e}")

# Categorical data distribution
print("Categorical Data Distribution:")
categorical_cols = df.select_dtypes(include=['object']).columns
for col in categorical_cols:
    print(f"{col}:\n{df[col].value_counts()}\n")

# Numerical data distribution
print("Numerical Data Distribution:")
numerical_cols = df.select_dtypes(include=['number']).columns
for col in numerical_cols:
    try:
        print(f"Processing {col}...")
        # Handle missing values by filling them with the column mean
        if df[col].isnull().sum() > 0:
            print(f"{col} has missing values. Filling with mean.")
            df[col] = df[col].fillna(df[col].mean())
        
        sns.histplot(df[col], kde=True)
        plt.title(f"Distribution of {col}")
        plt.savefig(f'visualization/{col}_distribution.png')
        plt.close()
        print(f"{col} distribution saved.\n")
    except Exception as e:
        print(f"Error processing {col}: {e}")

# Pairplot for numerical data
try:
    print("Creating pairplot...")
    sns.pairplot(df)
    plt.savefig('visualization/pairplot.png')
    plt.close()
    print("Pairplot saved.\n")
except Exception as e:
    print(f"Error creating pairplot: {e}")

# Correlation matrix
try:
    print("Creating correlation matrix...")
    corr_matrix = df.corr()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
    plt.title("Correlation Matrix")
    plt.savefig('visualization/correlation_matrix.png')
    plt.close()
    print("Correlation matrix saved.\n")
except Exception as e:
    print(f"Error creating correlation matrix: {e}")
