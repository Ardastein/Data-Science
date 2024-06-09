import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_cleaned_data(filepath):
    data = pd.read_csv(filepath)
    print("Columns in the dataset:", data.columns)
    print(data.head())  
    return data

def plot_sales_over_time(data, date_col, sales_col):
    """
    Plot the total pizza sales over time.
    """
    plt.figure(figsize=(12, 6))
    data[date_col] = pd.to_datetime(data[date_col])
    data.groupby(date_col)[sales_col].sum().plot()
    plt.title('Total Pizza Sales Over Time')
    plt.xlabel('Date')
    plt.ylabel('Total Sales ($)')
    plt.grid(True)
    plt.savefig('reports/figures/total_sales_over_time.png')
    plt.show()

def plot_sales_by_day(data, day_col, sales_col):
    """
    Plot pizza sales by day of the week.
    """
    plt.figure(figsize=(10, 5))
    sns.barplot(x=day_col, y=sales_col, data=data, estimator=sum)
    plt.title('Total Pizza Sales by Day of the Week')
    plt.xlabel('Day of the Week')
    plt.ylabel('Total Sales ($)')
    plt.savefig('reports/figures/sales_by_day_of_week.png')
    plt.show()

def plot_top_selling_pizzas(data, pizza_col, sales_col, top_n=10):
    """
    Plot the top N selling pizzas.
    """
    plt.figure(figsize=(12, 6))
    top_pizzas = data.groupby(pizza_col)[sales_col].sum().nlargest(top_n)
    sns.barplot(x=top_pizzas.index, y=top_pizzas.values)
    plt.title(f'Top {top_n} Selling Pizzas by Total Sales')
    plt.xlabel('Pizza Type')
    plt.ylabel('Total Sales ($)')
    plt.xticks(rotation=45)
    plt.savefig('reports/figures/top_selling_pizzas.png')
    plt.show()

if __name__ == "__main__":
    cleaned_filepath = 'data/cleaned_pizza_sales.csv'
    data = load_cleaned_data(cleaned_filepath)
    
    date_column = 'date'        
    sales_column = 'price'      
    pizza_column = 'name'       
    day_column = 'day_of_week'  

    plot_sales_over_time(data, date_column, sales_column)
    plot_sales_by_day(data, day_column, sales_column)
    plot_top_selling_pizzas(data, pizza_column, sales_column)
    print("Visualizations complete. Figures saved in 'reports/figures'.")
