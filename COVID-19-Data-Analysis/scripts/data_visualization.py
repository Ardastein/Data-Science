import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

def load_summary():
    summary = pd.read_csv('data/summary.csv')
    summary['Date'] = pd.to_datetime(summary['Date'])
    return summary

def plot_data(summary):
    plt.figure(figsize=(12, 8))
    plt.plot(summary['Date'], summary['Cases_confirmed'], label='Confirmed Cases')
    plt.plot(summary['Date'], summary['Cases_deaths'], label='Deaths')
    plt.plot(summary['Date'], summary['Cases_recovered'], label='Recovered')
    plt.xlabel('Date')
    plt.ylabel('Number of Cases')
    plt.title('COVID-19 Cases Over Time')
    plt.legend()
    plt.show()

def plot_interactive(summary):
    fig = px.line(summary, x='Date', y=['Cases_confirmed', 'Cases_deaths', 'Cases_recovered'], 
                  labels={'value':'Number of Cases', 'Date':'Date'},
                  title='COVID-19 Cases Over Time')
    fig.show()

if __name__ == "__main__":
    summary = load_summary()
    plot_data(summary)
    plot_interactive(summary)
