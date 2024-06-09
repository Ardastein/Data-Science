import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

project_structure = {
    "data": "data",
    "scripts": "scripts",
}

for key, path in project_structure.items():
    if not os.path.exists(path):
        os.makedirs(path)

def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print("Veri başarıyla yüklendi.")
        return df
    except Exception as e:
        print(f"Veri yüklenirken hata oluştu: {e}")
        return None

def explore_data(df):
    print("Verinin ilk 5 satırı:\n", df.head())
    print("\nVeri hakkında genel bilgi:\n", df.info())
    print("\nEksik değerlerin sayısı:\n", df.isnull().sum())
    print("\nVerinin özet istatistikleri:\n", df.describe())

def plot_data(df):
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Price'], kde=True)
    plt.title('Fiyat Dağılımı')
    plt.xlabel('Fiyat')
    plt.ylabel('Frekans')
    plt.savefig('scripts/price_distribution.png')
    plt.show()
    
    plt.figure(figsize=(12, 8))
    df.groupby('Description')['Price'].sum().plot(kind='bar')
    plt.title('Ürünlere Göre Toplam Harcama')
    plt.xlabel('Ürün')
    plt.ylabel('Toplam Harcama')
    plt.xticks(rotation=90)
    plt.tight_layout()  
    plt.savefig('scripts/description_expense.png')
    plt.show()

    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)  
    daily_expense = df.groupby('Date')['Price'].sum()
    
    plt.figure(figsize=(14, 7))
    daily_expense.plot()
    plt.title('Tarihlere Göre Günlük Harcama Trendi')
    plt.xlabel('Tarih')
    plt.ylabel('Toplam Harcama')
    plt.savefig('scripts/daily_expense_trend.png')
    plt.show()

def main():
    data_file_path = 'data/Swiss Bills.csv'
    df = load_data(data_file_path)
    
    if df is not None:
        explore_data(df)
        plot_data(df)

if __name__ == "__main__":
    main()
