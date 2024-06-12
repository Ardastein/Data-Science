import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data_path = 'data/african_crises.csv'
output_dir = 'output/figures/'

print("Reading dataset...")
df = pd.read_csv(data_path)
print("Dataset read successfully.")

print("First few rows of the dataframe:")
print(df.head())

print("\nBasic Info:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

df['banking_crisis_numeric'] = df['banking_crisis'].apply(lambda x: 1 if x == 'crisis' else 0)
print("Converted 'banking_crisis' to numeric.")

df['year'] = pd.to_datetime(df['year'], format='%Y')
print("Converted 'year' to datetime format.")

df_long = df.melt(id_vars=['country', 'year'], 
                  value_vars=['systemic_crisis', 'currency_crises', 'inflation_crises', 'banking_crisis_numeric'],
                  var_name='crisis_type', value_name='crisis_value')
print("Data prepared for plotting crisis types over time.")

sns.set(style="whitegrid")

def save_figure(fig, filename):
    fig.savefig(f"{output_dir}{filename}", bbox_inches='tight')
    plt.close(fig)

try:
    print("Plotting: Distribution of Crisis Events by Country")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.countplot(data=df, x='country', ax=ax)
    ax.set_title('Distribution of Crisis Events by Country')
    ax.set_ylabel('Number of Events')
    ax.set_xlabel('Country')
    save_figure(fig, 'crisis_events_by_country.png')
    print("Saved: crisis_events_by_country.png")
except Exception as e:
    print(f"Failed to plot crisis events by country: {e}")

try:
    print("Plotting: Distribution of Crisis Types Over Time")
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.lineplot(data=df_long, x='year', y='crisis_value', hue='crisis_type', ax=ax)
    ax.set_title('Crisis Types Over Time')
    ax.set_ylabel('Number of Events')
    ax.set_xlabel('Year')
    save_figure(fig, 'crisis_types_over_time.png')
    print("Saved: crisis_types_over_time.png")
except Exception as e:
    print(f"Failed to plot crisis types over time: {e}")

indicators = ['inflation_annual_cpi', 'gdp_weighted_default', 'exch_usd', 'reserves_usd']
for indicator in indicators:
    try:
        print(f"Plotting: Distribution of {indicator}")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.histplot(data=df, x=indicator, kde=True, ax=ax)
        ax.set_title(f'Distribution of {indicator}')
        save_figure(fig, f'distribution_{indicator}.png')
        print(f"Saved: distribution_{indicator}.png")
    except Exception as e:
        print(f"Failed to plot distribution for {indicator}: {e}")

try:
    print("Plotting: Correlation Heatmap")
    fig, ax = plt.subplots(figsize=(12, 10))
    corr = df.corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
    ax.set_title('Correlation Heatmap')
    save_figure(fig, 'correlation_heatmap.png')
    print("Saved: correlation_heatmap.png")
except Exception as e:
    print(f"Failed to plot correlation heatmap: {e}")

try:
    print("Plotting: Economic Indicators vs Systemic Crisis")
    fig, ax = plt.subplots(figsize=(14, 10))
    sns.pairplot(df, vars=indicators, hue='systemic_crisis', palette='coolwarm')
    plt.suptitle('Economic Indicators vs Systemic Crisis', y=1.02)
    save_figure(fig, 'indicators_vs_systemic_crisis.png')
    print("Saved: indicators_vs_systemic_crisis.png")
except Exception as e:
    print(f"Failed to plot economic indicators vs systemic crisis: {e}")

print("Analysis and visualizations completed. Check the 'output/figures' directory for saved figures.")
