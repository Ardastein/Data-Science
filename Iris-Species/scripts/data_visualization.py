import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'data/Iris.csv'
df = pd.read_csv(file_path)

df.columns = df.columns.str.lower()

sns.pairplot(df, hue='species')
plt.show()

plt.figure(figsize=(12, 8))
sns.boxplot(x='species', y='sepallengthcm', data=df)
plt.title('Sepal Length by Species')
plt.show()

plt.figure(figsize=(12, 8))
sns.violinplot(x='species', y='sepallengthcm', data=df)
plt.title('Sepal Length by Species')
plt.show()

plt.figure(figsize=(12, 8))
corr_matrix = df.drop(['id', 'species'], axis=1).corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

g = sns.PairGrid(df, hue='species')
g.map_diag(sns.histplot)
g.map_offdiag(sns.scatterplot)
g.add_legend()
plt.show()

plt.figure(figsize=(12, 8))
sns.histplot(df['sepallengthcm'], kde=True)
plt.title('Distribution of Sepal Length')
plt.show()
