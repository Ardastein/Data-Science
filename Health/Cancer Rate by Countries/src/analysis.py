import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data_path = 'C:/Users/HP/Desktop/Missions/Huawei/Health/Cancer Rate by Countries/data/Cancer_rate_by_countries.csv'
df = pd.read_csv(data_path)

print("Veri Kümesi Bilgisi:\n", df.info())
print("İlk 5 Satır:\n", df.head())

print("Boş Değerler:\n", df.isnull().sum())


sorted_df = df.sort_values(by='Cancer_Rate', ascending=False)
top_countries = sorted_df.head(20)

plt.figure(figsize=(12, 8))
sns.barplot(x='Cancer_Rate', y='Country', data=top_countries)
plt.title('Kanser Oranlarına Göre İlk 20 Ülke')
plt.xlabel('Kanser Oranı (Yüzde)')
plt.ylabel('Ülke')
plt.savefig('C:/Users/HP/Desktop/Missions/Huawei/Health/Cancer Rate by Countries/outputs/figures/top_20_countries_cancer_rate.png')
plt.show()

plt.figure(figsize=(12, 8))
sns.histplot(df['Cancer_Rate'], kde=True, bins=30)
plt.title('Kanser Oranlarının Dağılımı')
plt.xlabel('Kanser Oranı (Yüzde)')
plt.ylabel('Frekans')
plt.savefig('C:/Users/HP/Desktop/Missions/Huawei/Health/Cancer Rate by Countries/outputs/figures/cancer_rate_distribution.png')
plt.show()

plt.figure(figsize=(12, 8))
sns.boxplot(x='Cancer_Rate', data=df)
plt.title('Ülkelere Göre Kanser Oranlarının Kutu Grafiği')
plt.xlabel('Kanser Oranı (Yüzde)')
plt.savefig('C:/Users/HP/Desktop/Missions/Huawei/Health/Cancer Rate by Countries/outputs/figures/cancer_rate_boxplot.png')
plt.show()

print("Grafikler oluşturuldu ve kaydedildi.")
