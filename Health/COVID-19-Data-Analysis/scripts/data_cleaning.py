import pandas as pd

def load_data():
    confirmed = pd.read_csv('data/time_series_covid19_confirmed_global.csv')
    deaths = pd.read_csv('data/time_series_covid19_deaths_global.csv')
    recovered = pd.read_csv('data/time_series_covid19_recovered_global.csv')
    return confirmed, deaths, recovered

def clean_data(df):
    df = df.drop(['Lat', 'Long'], axis=1)
    df = df.melt(id_vars=['Province/State', 'Country/Region'], var_name='Date', value_name='Cases')
    df['Date'] = pd.to_datetime(df['Date'])
    return df

if __name__ == "__main__":
    confirmed, deaths, recovered = load_data()
    confirmed_clean = clean_data(confirmed)
    deaths_clean = clean_data(deaths)
    recovered_clean = clean_data(recovered)

    confirmed_clean.to_csv('data/cleaned_confirmed.csv', index=False)
    deaths_clean.to_csv('data/cleaned_deaths.csv', index=False)
    recovered_clean.to_csv('data/cleaned_recovered.csv', index=False)
