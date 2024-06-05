import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs('visualizations', exist_ok=True)

data_folder = 'C:/Users/HP/Desktop/Missions/Huawei/Education/University-Ranking/data/'

def load_data(file_path):
    try:
        return pd.read_csv(file_path, encoding='utf-8', on_bad_lines='skip')
    except Exception as e:
        print(f"Error loading {file_path}: {e}")
        return None

cwur_data = load_data(os.path.join(data_folder, 'cwurData.csv'))
edu_expenditure = load_data(os.path.join(data_folder, 'education_expenditure_supplementary_data.csv'))
edu_attainment = load_data(os.path.join(data_folder, 'educational_attainment_supplementary_data.csv'))
school_country = load_data(os.path.join(data_folder, 'school_and_country_table.csv'))
shanghai_data = load_data(os.path.join(data_folder, 'shanghaiData.csv'))
times_data = load_data(os.path.join(data_folder, 'timesData.csv'))

for df, name in zip([cwur_data, edu_expenditure, edu_attainment, school_country, shanghai_data, times_data],
                    ['cwur_data', 'edu_expenditure', 'edu_attainment', 'school_country', 'shanghai_data', 'times_data']):
    if df is not None:
        print(f"{name} info:")
        print(df.info())
        print(df.describe())
    else:
        print(f"{name} could not be loaded.")

def plot_histogram(df, column, title, filename):
    if df is not None and column in df.columns:
        plt.figure(figsize=(10, 6))
        sns.histplot(df[column], kde=True)
        plt.title(title)
        plt.savefig(f'visualizations/{filename}')
        plt.close()

def plot_bar(df, column, title, filename):
    if df is not None and column in df.columns:
        plt.figure(figsize=(10, 6))
        sns.countplot(x=column, data=df)
        plt.title(title)
        plt.savefig(f'visualizations/{filename}')
        plt.close()

def plot_box(df, column, title, filename):
    if df is not None and column in df.columns:
        plt.figure(figsize=(10, 6))
        sns.boxplot(x=column, data=df)
        plt.title(title)
        plt.savefig(f'visualizations/{filename}')
        plt.close()

def plot_heatmap(df, title, filename):
    if df is not None:
        numeric_df = df.select_dtypes(include=['float64', 'int64'])
        plt.figure(figsize=(12, 8))
        sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', linewidths=.5)
        plt.title(title)
        plt.savefig(f'visualizations/{filename}')
        plt.close()

plot_histogram(cwur_data, 'world_rank', 'World Rank Distribution', 'cwur_world_rank_distribution.png')
plot_bar(cwur_data, 'country', 'Country Distribution', 'cwur_country_distribution.png')
plot_box(cwur_data, 'score', 'Score Distribution', 'cwur_score_distribution.png')
plot_heatmap(cwur_data, 'CWUR Data Correlation Heatmap', 'cwur_correlation_heatmap.png')

plot_histogram(shanghai_data, 'world_rank', 'Shanghai World Rank Distribution', 'shanghai_world_rank_distribution.png')
plot_bar(shanghai_data, 'country', 'Shanghai Country Distribution', 'shanghai_country_distribution.png')
plot_box(shanghai_data, 'total_score', 'Shanghai Total Score Distribution', 'shanghai_total_score_distribution.png')
plot_heatmap(shanghai_data, 'Shanghai Data Correlation Heatmap', 'shanghai_correlation_heatmap.png')

plot_histogram(times_data, 'world_rank', 'Times World Rank Distribution', 'times_world_rank_distribution.png')
plot_bar(times_data, 'country', 'Times Country Distribution', 'times_country_distribution.png')
plot_box(times_data, 'total_score', 'Times Total Score Distribution', 'times_total_score_distribution.png')
plot_heatmap(times_data, 'Times Data Correlation Heatmap', 'times_correlation_heatmap.png')

if edu_expenditure is not None:
    plot_histogram(edu_expenditure, 'value', 'Education Expenditure Distribution', 'edu_expenditure_distribution.png')
    plot_box(edu_expenditure, 'value', 'Education Expenditure Boxplot', 'edu_expenditure_boxplot.png')
    plot_heatmap(edu_expenditure, 'Education Expenditure Correlation Heatmap', 'edu_expenditure_correlation_heatmap.png')

plot_histogram(edu_attainment, 'value', 'Educational Attainment Distribution', 'edu_attainment_distribution.png')
plot_box(edu_attainment, 'value', 'Educational Attainment Boxplot', 'edu_attainment_boxplot.png')
plot_heatmap(edu_attainment, 'Educational Attainment Correlation Heatmap', 'edu_attainment_correlation_heatmap.png')
