import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import os
from datetime import datetime

cleaned_data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data'))
output_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../output'))
train = pd.read_csv(os.path.join(cleaned_data_path, 'cleaned_train.csv'))
test = pd.read_csv(os.path.join(cleaned_data_path, 'cleaned_test.csv'))
model = joblib.load(os.path.join(output_path, 'sales_forecasting_model.pkl'))

def plot_real_vs_pred():
    y_val = train['Weekly_Sales']
    y_pred = model.predict(train.drop('Weekly_Sales', axis=1))

    plt.figure(figsize=(14, 7))
    plt.plot(y_val.values, label='Gerçek Değerler')
    plt.plot(y_pred, label='Tahminler')
    plt.legend()
    plt.title('Gerçek ve Tahmin Edilen Değerler')
    plt.show()

def plot_feature_importance():
    feature_importances = model.feature_importances_
    features = train.drop('Weekly_Sales', axis=1).columns
    feature_df = pd.DataFrame({'Feature': features, 'Importance': feature_importances})
    feature_df = feature_df.sort_values(by='Importance', ascending=False)

    plt.figure(figsize=(14, 7))
    sns.barplot(x='Importance', y='Feature', data=feature_df)
    plt.title('Özellik Önem Grafiği')
    plt.show()

def plot_time_series():
    train['Date'] = train.apply(lambda row: datetime.strptime(f"{int(row.Year)}-{int(row.Month)}-{int(row.Week)}", "%Y-%m-%W"), axis=1)
    sales_by_date = train.groupby('Date')['Weekly_Sales'].sum().reset_index()

    plt.figure(figsize=(14, 7))
    plt.plot(sales_by_date['Date'], sales_by_date['Weekly_Sales'])
    plt.title('Zaman Serisi Analizi')
    plt.xlabel('Tarih')
    plt.ylabel('Toplam Satış')
    plt.show()

def plot_sales_by_store():
    sales_by_store = train.groupby('Store')['Weekly_Sales'].sum().reset_index()

    plt.figure(figsize=(14, 7))
    sns.barplot(x='Store', y='Weekly_Sales', data=sales_by_store)
    plt.title('Mağaza Bazında Satış Analizi')
    plt.xlabel('Mağaza')
    plt.ylabel('Toplam Satış')
    plt.show()

def plot_sales_by_year_month():
    sales_by_year_month = train.groupby(['Year', 'Month'])['Weekly_Sales'].sum().reset_index()

    plt.figure(figsize=(14, 7))
    sns.lineplot(x='Month', y='Weekly_Sales', hue='Year', data=sales_by_year_month, marker='o')
    plt.title('Yıl ve Ay Bazında Satış Analizi')
    plt.xlabel('Ay')
    plt.ylabel('Toplam Satış')
    plt.show()

def plot_scatter_plots():
    plt.figure(figsize=(14, 7))
    sns.scatterplot(x='CPI', y='Weekly_Sales', data=train)
    plt.title('CPI ve Satış Dağılımı')
    plt.xlabel('CPI')
    plt.ylabel('Satış')
    plt.show()

    plt.figure(figsize=(14, 7))
    sns.scatterplot(x='Unemployment', y='Weekly_Sales', data=train)
    plt.title('İşsizlik Oranı ve Satış Dağılımı')
    plt.xlabel('İşsizlik Oranı')
    plt.ylabel('Satış')
    plt.show()

plot_real_vs_pred()
plot_feature_importance()
plot_time_series()
plot_sales_by_store()
plot_sales_by_year_month()
plot_scatter_plots()
