import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

def create_visualizations(data):
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='State', y='Rating', data=data)
    plt.title('Rating Distribution by State')
    plt.xticks(rotation=90)
    plt.savefig('eda/Rating_By_State.png')
    plt.show()

    fig = px.scatter(data, x='Rating', y='UG_fee', color='State', title='Rating vs UG Fee')
    fig.write_html('eda/Rating_vs_UG_Fee.html')
    fig.show()

if __name__ == "__main__":
    file_path = "data/Cleaned_Top_Indian_Colleges.csv"
    data = load_data(file_path)
    create_visualizations(data)
