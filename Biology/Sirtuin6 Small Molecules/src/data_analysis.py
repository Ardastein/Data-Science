import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

data_path = "data/SIRTUIN6.csv"
plots_path = "data/plots"

os.makedirs(plots_path, exist_ok=True)

df = pd.read_csv(data_path)

print("Dataset Info:")
print(df.info())
print("\n")

print("First 5 Rows:")
print(df.head())
print("\n")

print("Summary Statistics:")
print(df.describe())
print("\n")

print("Missing Values:")
print(df.isnull().sum())
print("\n")

with open("data/summary_info.txt", "w") as f:
    df.info(buf=f)
    f.write("\nSummary Statistics:\n")
    f.write(str(df.describe()))
    f.write("\nMissing Values:\n")
    f.write(str(df.isnull().sum()))

sns.set(style="whitegrid")

numerical_features = df.select_dtypes(include=['float64', 'int64']).columns

for feature in numerical_features:
    plt.figure(figsize=(10, 6))
    sns.histplot(df[feature], kde=True, bins=30)
    plt.title(f'Distribution of {feature}')
    plt.xlabel(feature)
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.savefig(f"{plots_path}/distribution_{feature}.png")
    plt.show()

plt.figure(figsize=(10, 6))
sns.pairplot(df[numerical_features])  
plt.title("Pairplot of Numerical Features")
plt.savefig(f"{plots_path}/pairplot.png")
plt.show()

plt.figure(figsize=(12, 8))
correlation_matrix = df[numerical_features].corr()  
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Correlation Heatmap")
plt.savefig(f"{plots_path}/correlation_heatmap.png")
plt.show()

plt.figure(figsize=(10, 6))
if len(numerical_features) > 1:
    sns.scatterplot(data=df, x=numerical_features[0], y=numerical_features[1])
    plt.title(f'Scatter Plot between {numerical_features[0]} and {numerical_features[1]}')
    plt.xlabel(numerical_features[0])
    plt.ylabel(numerical_features[1])
    plt.grid(True)
    plt.savefig(f"{plots_path}/scatter_{numerical_features[0]}_{numerical_features[1]}.png")
    plt.show()
else:
    print("Not enough numerical features for scatter plot.")

for feature in numerical_features:
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df[feature])
    plt.title(f'Box Plot of {feature}')
    plt.xlabel(feature)
    plt.grid(True)
    plt.savefig(f"{plots_path}/boxplot_{feature}.png")
    plt.show()

plt.figure(figsize=(12, 8))
sns.boxplot(x='Class', y='SC-5', data=df)
plt.title('Box Plot of SC-5 by Class')
plt.xlabel('Class')
plt.ylabel('SC-5')
plt.grid(True)
plt.savefig(f"{plots_path}/boxplot_SC-5_Class.png")
plt.show()

for feature in numerical_features:
    if feature != 'SC-5':  
        plt.figure(figsize=(12, 8))
        sns.boxplot(x='Class', y=feature, data=df)
        plt.title(f'Box Plot of {feature} by Class')
        plt.xlabel('Class')
        plt.ylabel(feature)
        plt.grid(True)
        plt.savefig(f"{plots_path}/boxplot_{feature}_Class.png")
        plt.show()
