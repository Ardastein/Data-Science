import pandas as pd

def load_cleaned_data():
    confirmed = pd.read_csv('data/cleaned_confirmed.csv')
    deaths = pd.read_csv('data/cleaned_deaths.csv')
    recovered = pd.read_csv('data/cleaned_recovered.csv')
    return confirmed, deaths, recovered

def analyze_data(confirmed, deaths, recovered):
    summary = confirmed.groupby('Date')['Cases'].sum().reset_index()
    summary = summary.merge(deaths.groupby('Date')['Cases'].sum().reset_index(), on='Date', suffixes=('_confirmed', '_deaths'))
    summary = summary.merge(recovered.groupby('Date')['Cases'].sum().reset_index(), on='Date')
    summary.rename(columns={'Cases': 'Cases_recovered'}, inplace=True)
    return summary

if __name__ == "__main__":
    confirmed, deaths, recovered = load_cleaned_data()
    summary = analyze_data(confirmed, deaths, recovered)
    summary.to_csv('data/summary.csv', index=False)
