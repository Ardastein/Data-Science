import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

def eda(data):
    print(data.info())
    print(data.describe())
    print(data.isnull().sum())
    print(data['State'].value_counts())

    plt.figure(figsize=(10, 6))
    sns.countplot(y='State', data=data, order=data['State'].value_counts().index)
    plt.title('Number of Colleges in Each State')
    plt.savefig('eda/State_Counts.png')
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.histplot(data['Rating'])
    plt.title('Distribution of Ratings')
    plt.savefig('eda/Rating_Distribution.png')
    plt.show()

if __name__ == "__main__":
    file_path = "data/Cleaned_Top_Indian_Colleges.csv"
    data = load_data(file_path)
    eda(data)
