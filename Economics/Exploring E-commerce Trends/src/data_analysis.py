import matplotlib.pyplot as plt
import seaborn as sns

def plot_histogram(data, column, title, xlabel, ylabel, bins=30):
    """
    Plot a histogram for a specific column.

    :param data: DataFrame, the dataset to plot
    :param column: str, the column to plot
    :param title: str, the title of the plot
    :param xlabel: str, label for the x-axis
    :param ylabel: str, label for the y-axis
    :param bins: int, number of bins in the histogram
    """
    plt.figure(figsize=(10, 6))
    sns.histplot(data[column], bins=bins, kde=True)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()

def plot_bar(data, column, title, xlabel, ylabel):
    """
    Plot a bar chart for a specific column.

    :param data: DataFrame, the dataset to plot
    :param column: str, the column to plot
    :param title: str, the title of the plot
    :param xlabel: str, label for the x-axis
    :param ylabel: str, label for the y-axis
    """
    plt.figure(figsize=(10, 6))
    data[column].value_counts().plot(kind='bar')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()

def plot_scatter(data, x_col, y_col, title, xlabel, ylabel):
    """
    Plot a scatter plot between two columns.

    :param data: DataFrame, the dataset to plot
    :param x_col: str, the column for the x-axis
    :param y_col: str, the column for the y-axis
    :param title: str, the title of the plot
    :param xlabel: str, label for the x-axis
    :param ylabel: str, label for the y-axis
    """
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=data, x=x_col, y=y_col)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()

def plot_box(data, column, title, xlabel, ylabel):
    """
    Plot a box plot for a specific column.

    :param data: DataFrame, the dataset to plot
    :param column: str, the column to plot
    :param title: str, the title of the plot
    :param xlabel: str, label for the x-axis
    :param ylabel: str, label for the y-axis
    """
    plt.figure(figsize=(10, 6))
    sns.boxplot(data[column])
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()
