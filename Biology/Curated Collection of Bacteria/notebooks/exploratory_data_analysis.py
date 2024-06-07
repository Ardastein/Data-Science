import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# Veriyi yükleme
data = pd.read_csv('data/bacteria_list_200.csv')

# 'Harmful to Humans' değerlerini kontrol et ve kategorik olarak encode et
data['Harmful to Humans'] = data['Harmful to Humans'].map({'Yes': 1, 'No': 0})

# Zararlı olanları filtreleme ve en sık görülen aileleri bulma
harmful_bacteria = data[data['Harmful to Humans'] == 1]
top_families = harmful_bacteria['Family'].value_counts().nlargest(10).index
filtered_data = harmful_bacteria[harmful_bacteria['Family'].isin(top_families)]

# İsimlerin kısaltılması
filtered_data['Short Name'] = filtered_data['Name'].apply(lambda x: ' '.join(x.split()[:2]))

# 1. En Çok Görülen Zararlı Bakteri Aileleri Bar Grafiği
plt.figure(figsize=(12, 6))
sns.countplot(y='Family', data=filtered_data, order=filtered_data['Family'].value_counts().index, palette='viridis')
plt.title('En Çok Görülen 10 Zararlı Bakteri Ailesi')
plt.xlabel('Bakteri Sayısı')
plt.ylabel('Aile')
plt.show()

# 2. Etkileşimli Bakteri Dağılımı Grafiği
fig = px.scatter(filtered_data, x='Short Name', y='Family', color='Harmful to Humans',
                 title='Zararlı Bakterilerin Dağılımı', labels={'Harmful to Humans': 'Zararlılık Durumu'})
fig.update_layout(xaxis_tickangle=-45, height=800, width=1000)
fig.show()

# 3. Bakteri İsimlerinin Kısaltılması ve Aile Dağılımı
top_names = data['Name'].value_counts().nlargest(15).index
name_filtered_data = data[data['Name'].isin(top_names)]

plt.figure(figsize=(14, 7))
sns.countplot(y='Name', data=name_filtered_data, order=name_filtered_data['Name'].value_counts().index, palette='viridis')
plt.title('En Çok Görülen 15 Bakteri İsmi ve Aile Dağılımı')
plt.xlabel('Bakteri Sayısı')
plt.ylabel('Bakteri İsimleri')
plt.show()
