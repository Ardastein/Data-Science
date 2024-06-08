import pandas as pd

def load_data(file_path):
    """ Load the real estate data from a CSV file. """
    df = pd.read_csv(file_path)
    return df

def clean_data(df):
    """ Clean the real estate data by handling missing values and data types. """
    if 'Average Sales Price' in df.columns:
        df['price'] = df['Average Sales Price'].astype(float)
    else:
        print("Average Sales Price column not found. Available columns:", df.columns)
    
    month_to_number = {
        'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
        'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12
    }
    
    if 'Month' in df.columns:
        df['Month'] = df['Month'].map(month_to_number)

    df = df.dropna()

    return df

def summarize_data(df):
    """ Provide basic summary statistics of the dataset. """
    summary = df.describe()
    return summary
