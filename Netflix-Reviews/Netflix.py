import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import pickle
import os

data_path = 'C:/Users/HP/Desktop/Missions/Huawei/Netflix-Reviews/data/netflix_reviews.csv'  # Doğru dosya yolunu belirtiyoruz
visualizations_path = './visualizations/'
models_path = './models/'

os.makedirs(visualizations_path, exist_ok=True)
os.makedirs(models_path, exist_ok=True)

df = pd.read_csv(data_path)

print(df.head())

print(df.info())

print(df.isnull().sum())

df = df[['content', 'score']].dropna()

df['sentiment'] = df['score'].apply(lambda x: 'positive' if x > 3 else 'negative')

print(df['sentiment'].value_counts())

def preprocess_text(text):
    text = text.lower()
    text = ''.join([c for c in text if c not in ('!', '.', ':', ',', '?', '-', '(', ')', '[', ']', '{', '}', '\'')])
    return text

df['cleaned_review_text'] = df['content'].apply(preprocess_text)

X = df['cleaned_review_text']
y = df['sentiment']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

vectorizer = CountVectorizer()
X_train_bow = vectorizer.fit_transform(X_train)
X_test_bow = vectorizer.transform(X_test)

lr_model = LogisticRegression()
lr_model.fit(X_train_bow, y_train)

y_pred_bow = lr_model.predict(X_test_bow)

accuracy_bow = accuracy_score(y_test, y_pred_bow)
print(f'Bag of Words Model Accuracy: {accuracy_bow}')

with open(os.path.join(models_path, 'logistic_regression_bow.pkl'), 'wb') as model_file:
    pickle.dump(lr_model, model_file)

conf_matrix_bow = confusion_matrix(y_test, y_pred_bow)
class_report_bow = classification_report(y_test, y_pred_bow)

positive_reviews = df[df['sentiment'] == 'positive']['cleaned_review_text']
negative_reviews = df[df['sentiment'] == 'negative']['cleaned_review_text']

positive_text = ' '.join(positive_reviews)
negative_text = ' '.join(negative_reviews)

wordcloud_positive = WordCloud(width=800, height=400, background_color='white').generate(positive_text)
wordcloud_negative = WordCloud(width=800, height=400, background_color='black').generate(negative_text)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(wordcloud_positive, interpolation='bilinear')
plt.axis('off')
plt.title('Positive Reviews')
plt.savefig(os.path.join(visualizations_path, 'wordcloud_positive.png'))

plt.subplot(1, 2, 2)
plt.imshow(wordcloud_negative, interpolation='bilinear')
plt.axis('off')
plt.title('Negative Reviews')
plt.savefig(os.path.join(visualizations_path, 'wordcloud_negative.png'))

plt.show()

plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix_bow, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix for Bag of Words Model')
plt.savefig(os.path.join(visualizations_path, 'confusion_matrix_bow.png'))
plt.show()

print(class_report_bow)

accuracy_values = [accuracy_bow]  
model_names = ['Logistic Regression (BoW)']

plt.figure(figsize=(10, 6))
plt.bar(model_names, accuracy_values, color='skyblue')
plt.xlabel('Model')
plt.ylabel('Accuracy')
plt.ylim(0, 1)
plt.title('Model Accuracy Comparison')
plt.savefig(os.path.join(visualizations_path, 'accuracy_plot.png'))
plt.show()
