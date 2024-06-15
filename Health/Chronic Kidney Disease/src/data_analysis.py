import pandas as pd

def basic_statistics(data):
    return data.describe()

def value_counts(data, column):
    return data[column].value_counts()
