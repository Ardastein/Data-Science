import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import matplotlib
matplotlib.use('Agg')

data_path = 'data/Kaggle_Datasets.csv'
df = pd.read_csv(data_path)

plt.style.use('ggplot')
sns.set_palette('Set2')

top_10_datasets = df['title'].value_counts().head(10)
plt.figure(figsize=(12, 6))
top_10_datasets.plot(kind='bar')
plt.title('Top 10 Datasets by Count')
plt.ylabel('Count')
plt.xlabel('Dataset Title')
plt.xticks(rotation=45)
plt.savefig('visualization/top_10_datasets.png')
plt.close()

plt.figure(figsize=(12, 6))
sns.scatterplot(data=df, x='views', y='upvotes', hue='category')
plt.title('Upvotes vs. Views by Category')
plt.ylabel('Upvotes')
plt.xlabel('Views')
plt.legend(title='Category')
plt.savefig('visualization/upvotes_vs_views.png')
plt.close()

plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='category', y='upvotes')
plt.title('Upvotes by Category')
plt.ylabel('Upvotes')
plt.xlabel('Category')
plt.xticks(rotation=45)
plt.savefig('visualization/upvotes_by_category.png')
plt.close()
