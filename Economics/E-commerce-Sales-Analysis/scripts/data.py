import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    data = pd.read_csv('data/e_commerce_data.csv', encoding='latin1')
    return data

def clean_data(df):
    print("Columns in the DataFrame:", df.columns)  
    if 'InvoiceDate' in df.columns:
        df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    else:
        print("Error: 'InvoiceDate' column not found in the DataFrame.")
    return df

def analyze_data(df):
    country_sales = df.groupby('Country')['Quantity'].sum().sort_values(ascending=False)
    print(country_sales.head())
    return country_sales

def visualize_data(df):
    country_sales = df.groupby('Country')['Quantity'].sum().sort_values(ascending=False)
    top_countries = country_sales.head(10)
    plt.figure(figsize=(10, 6))
    top_countries.plot(kind='bar', color='skyblue')
    plt.title('Top 10 Countries by Quantity Sold')
    plt.xlabel('Country')
    plt.ylabel('Total Quantity Sold')
    plt.xticks(rotation=45)
    plt.show()
    
    df['Month'] = df['InvoiceDate'].dt.to_period('M')
    monthly_sales = df.groupby('Month')['Quantity'].sum()
    plt.figure(figsize=(10, 6))
    monthly_sales.plot(kind='line', marker='o', color='green')
    plt.title('Monthly Sales')
    plt.xlabel('Month')
    plt.ylabel('Total Quantity Sold')
    plt.xticks(rotation=45)
    plt.show()
    
    top_products = df.groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(10)
    plt.figure(figsize=(10, 6))
    top_products.plot(kind='bar', color='purple')
    plt.title('Top 10 Products by Quantity Sold')
    plt.xlabel('Product')
    plt.ylabel('Total Quantity Sold')
    plt.xticks(rotation=45)
    plt.show()
    
    df['Revenue'] = df['Quantity'] * df['UnitPrice']
    country_revenue = df.groupby('Country')['Revenue'].sum().sort_values(ascending=False).head(5)
    plt.figure(figsize=(10, 6))
    country_revenue.plot(kind='pie', autopct='%1.1f%%', startangle=140, colormap='tab20')
    plt.title('Revenue by Country (Top 5)')
    plt.ylabel('')
    plt.show()
    
    monthly_revenue = df.groupby('Month')['Revenue'].sum()
    plt.figure(figsize=(10, 6))
    monthly_revenue.plot(kind='line', marker='o', color='red')
    plt.title('Monthly Revenue')
    plt.xlabel('Month')
    plt.ylabel('Total Revenue')
    plt.xticks(rotation=45)
    plt.show()
    
    product_revenue = df.groupby('Description')['Revenue'].sum().sort_values(ascending=False).head(10)
    plt.figure(figsize=(10, 6))
    product_revenue.plot(kind='bar', color='orange')
    plt.title('Top 10 Products by Revenue')
    plt.xlabel('Product')
    plt.ylabel('Total Revenue')
    plt.xticks(rotation=45)
    plt.show()
    
    invoice_quantity = df.groupby('InvoiceNo')['Quantity'].sum().sort_values(ascending=False).head(10)
    plt.figure(figsize=(10, 6))
    invoice_quantity.plot(kind='bar', color='cyan')
    plt.title('Top 10 Invoices by Quantity')
    plt.xlabel('Invoice No')
    plt.ylabel('Total Quantity')
    plt.xticks(rotation=45)
    plt.show()
    
    invoice_revenue = df.groupby('InvoiceNo')['Revenue'].sum().sort_values(ascending=False).head(10)
    plt.figure(figsize=(10, 6))
    invoice_revenue.plot(kind='bar', color='magenta')
    plt.title('Top 10 Invoices by Revenue')
    plt.xlabel('Invoice No')
    plt.ylabel('Total Revenue')
    plt.xticks(rotation=45)
    plt.show()

data = load_data()
cleaned_data = clean_data(data)
visualize_data(cleaned_data)
