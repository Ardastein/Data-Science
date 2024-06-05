import pandas as pd
import numpy as np
import os

base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data'))
features_path = os.path.join(base_path, 'features.csv')
stores_path = os.path.join(base_path, 'stores.csv')
train_path = os.path.join(base_path, 'train.csv')
test_path = os.path.join(base_path, 'test.csv')

features = pd.read_csv(features_path)
stores = pd.read_csv(stores_path)
train = pd.read_csv(train_path)
test = pd.read_csv(test_path)

features.fillna(0, inplace=True)
train.fillna(0, inplace=True)
test.fillna(0, inplace=True)

features['Date'] = pd.to_datetime(features['Date'])
train['Date'] = pd.to_datetime(train['Date'])
test['Date'] = pd.to_datetime(test['Date'])

train = train.merge(features, on=['Store', 'Date', 'IsHoliday'], how='left')
train = train.merge(stores, on=['Store'], how='left')
test = test.merge(features, on=['Store', 'Date', 'IsHoliday'], how='left')
test = test.merge(stores, on=['Store'], how='left')

train['Year'] = train['Date'].dt.year
train['Month'] = train['Date'].dt.month
train['Week'] = train['Date'].dt.isocalendar().week
test['Year'] = test['Date'].dt.year
test['Month'] = test['Date'].dt.month
test['Week'] = test['Date'].dt.isocalendar().week

train.drop(['Date', 'IsHoliday'], axis=1, inplace=True)
test.drop(['Date', 'IsHoliday'], axis=1, inplace=True)

train = pd.get_dummies(train, columns=['Type'], drop_first=True)
test = pd.get_dummies(test, columns=['Type'], drop_first=True)

cleaned_data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data'))
train.to_csv(os.path.join(cleaned_data_path, 'cleaned_train.csv'), index=False)
test.to_csv(os.path.join(cleaned_data_path, 'cleaned_test.csv'), index=False)
