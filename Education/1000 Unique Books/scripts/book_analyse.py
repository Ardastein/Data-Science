import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

csv_file = r'data/bookstoscrape.csv'  
output_folder = r'C:\Users\HP\Desktop\Missions\Huawei\Education\1000 Unique Books\outputs'  

books = pd.read_csv(csv_file)

print(books.head())

print(books.info())

rating_counts = books['Star Rating'].value_counts()
plt.figure(figsize=(10,6))
sns.barplot(x=rating_counts.index, y=rating_counts.values, hue=rating_counts.index, palette='viridis', dodge=False, legend=False)
plt.xlabel('Yıldız')
plt.ylabel('Kitap Sayısı')
plt.title('Yıldız Sayısına Göre Kitap Sayısı')
plt.tight_layout()
plt.savefig(os.path.join(output_folder, 'rating_counts.png'))
plt.show()

plt.figure(figsize=(10,6))
sns.histplot(books['Price'], bins=30, kde=True, color='blue')
plt.xlabel('Fiyat (£)')
plt.ylabel('Kitap Sayısı')
plt.title('Kitap Fiyatlarının Dağılımı')
plt.tight_layout()
plt.savefig(os.path.join(output_folder, 'price_distribution.png'))
plt.show()

plt.figure(figsize=(10,6))
sns.boxplot(x='Star Rating', y='Price', data=books, hue='Star Rating', palette='coolwarm', dodge=False, legend=False)
plt.xlabel('Yıldız')
plt.ylabel('Fiyat (£)')
plt.title('Fiyat ve Yıldız İlişkisi')
plt.tight_layout()
plt.savefig(os.path.join(output_folder, 'price_vs_rating.png'))
plt.show()

avg_price_by_rating = books.groupby('Star Rating')['Price'].mean().sort_values(ascending=False)
plt.figure(figsize=(10,6))
sns.barplot(x=avg_price_by_rating.index, y=avg_price_by_rating.values, hue=avg_price_by_rating.index, palette='viridis', dodge=False, legend=False)
plt.xlabel('Yıldız')
plt.ylabel('Ortalama Fiyat (£)')
plt.title('Yıldız Derecelendirmelerine Göre Ortalama Kitap Fiyatı')
plt.tight_layout()
plt.savefig(os.path.join(output_folder, 'avg_price_by_rating.png'))
plt.show()