import pandas as pd
import joblib
import os

cleaned_data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data'))
test = pd.read_csv(os.path.join(cleaned_data_path, 'cleaned_test.csv'))

print(test.columns)

output_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../output'))
model = joblib.load(os.path.join(output_path, 'sales_forecasting_model.pkl'))

if 'Id' in test.columns:
    test_predictions = model.predict(test.drop('Id', axis=1))
else:
    test_predictions = model.predict(test)

if 'Id' in test.columns:
    submission = pd.DataFrame({'Id': test['Id'], 'Weekly_Sales': test_predictions})
else:
    submission = pd.DataFrame({'Weekly_Sales': test_predictions})

submission.to_csv(os.path.join(output_path, 'submission.csv'), index=False)
