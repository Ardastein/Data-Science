import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def eda(df):
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    
    plt.figure(figsize=(10, 6))
    sns.heatmap(numeric_df.corr(), annot=True, fmt=".2f")
    plt.show()
    
    df.hist(figsize=(20, 15))
    plt.show()
    
    sns.pairplot(df, hue='diagnosis')
    plt.show()
    
    sns.countplot(x='diagnosis', data=df)
    plt.show()
