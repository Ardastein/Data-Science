import pandas as pd

def load_data(filepath):
    """
    Load the pizza sales data from a CSV file.
    """
    data = pd.read_csv(filepath)
    return data

def preprocess_data(data):
    """
    Preprocess the data:
    - Convert date columns to datetime
    - Handle missing values
    - Extract additional features if necessary
    """
    data['date'] = pd.to_datetime(data['date'], errors='coerce')

    data = data.dropna()


    data['day_of_week'] = data['date'].dt.day_name()

    return data

if __name__ == "__main__":
    filepath = 'data/A_year_of_pizza_sales_from_a_pizza_place_872_68.csv'
    data = load_data(filepath)
    clean_data = preprocess_data(data)
    clean_data.to_csv('data/cleaned_pizza_sales.csv', index=False)
    print("Data preprocessing complete. Cleaned data saved to 'cleaned_pizza_sales.csv'.")
