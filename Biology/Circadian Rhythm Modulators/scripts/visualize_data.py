import pandas as pd
import matplotlib.pyplot as plt
import os

data_path = 'data'
data_csv = os.path.join(data_path, 'data.csv')
period_changer_csv = os.path.join(data_path, 'Period-Changer-10F.csv')

data_df = pd.read_csv(data_csv)
period_changer_df = pd.read_csv(period_changer_csv)

print("data.csv dosyasının ilk birkaç satırı:")
print(data_df.head())
print("\nPeriod-Changer-10F.csv dosyasının ilk birkaç satırı:")
print(period_changer_df.head())

results_path = os.path.join(data_path, 'results')
if not os.path.exists(results_path):
    os.makedirs(results_path)

def draw_histogram(df, column, title, xlabel, ylabel, filename):
    plt.figure(figsize=(10, 6))
    plt.hist(df[column].dropna(), bins=20, edgecolor='black')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.savefig(os.path.join(results_path, filename))
    plt.close()

def draw_line_plot(df, x_column, y_column, title, xlabel, ylabel, filename):
    plt.figure(figsize=(10, 6))
    plt.plot(df[x_column], df[y_column], marker='o')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.savefig(os.path.join(results_path, filename))
    plt.close()

def draw_scatter_plot(df, x_column, y_column, title, xlabel, ylabel, filename):
    plt.figure(figsize=(10, 6))
    plt.scatter(df[x_column], df[y_column], alpha=0.7)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.savefig(os.path.join(results_path, filename))
    plt.close()

def draw_bar_plot(df, x_column, y_column, title, xlabel, ylabel, filename):
    plt.figure(figsize=(10, 6))
    plt.bar(df[x_column], df[y_column], color='skyblue', edgecolor='black')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=90)
    plt.grid(axis='y')
    plt.savefig(os.path.join(results_path, filename))
    plt.close()


if 'MATS3v' in data_df.columns:
    draw_histogram(data_df, 'MATS3v', 'Histogram of MATS3v', 'MATS3v', 'Frequency', 'histogram_mats3v.png')

if 'ATSC8c' in period_changer_df.columns and 'MATS1e' in period_changer_df.columns:
    draw_line_plot(period_changer_df, 'ATSC8c', 'MATS1e', 'Line Plot of MATS1e over ATSC8c', 'ATSC8c', 'MATS1e', 'line_plot_ATSC8c_vs_MATS1e.png')

if 'MATS3v' in data_df.columns and 'MATS3s' in data_df.columns:
    draw_scatter_plot(data_df, 'MATS3v', 'MATS3s', 'Scatter Plot of MATS3v vs MATS3s', 'MATS3v', 'MATS3s', 'scatter_plot_MATS3v_vs_MATS3s.png')

if 'Class ' in period_changer_df.columns and 'ATSC8c' in period_changer_df.columns:
    bar_data = period_changer_df.groupby('Class ')['ATSC8c'].mean().reset_index()
    draw_bar_plot(bar_data, 'Class ', 'ATSC8c', 'Bar Plot of Average ATSC8c by Class', 'Class', 'Average ATSC8c', 'bar_plot_ATSC8c_by_Class.png')

print("Grafikler başarıyla oluşturuldu ve kaydedildi.")
