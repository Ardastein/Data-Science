# Sales Forecasting Project

This project aims to build a sales forecasting model using historical sales data.

# Sales Forecasting Project

This project aims to predict sales using historical data from a retail dataset. It involves data preprocessing, model training, prediction, and visualization using Python and Power BI. The dataset includes historical sales data, store information, and additional features such as holidays and weather data. The dataset files are `features.csv`, `stores.csv`, `train.csv`, and `test.csv`.

## Data Cleaning

The data cleaning process involves:
- Loading datasets from CSV files.
- Converting date columns to datetime format.
- Merging datasets to form a comprehensive training set.
- Handling missing values and removing any irrelevant data.
- Creating new features such as year, month, and week.

## Visualizations

### Real vs Predicted Values
This line chart compares the actual sales with the predicted sales values.

![Real vs Predicted Values](https://github.com/Fuatorium/Huawei/blob/main/sales_forecasting/graphs/Figure_1.png)

### Feature Importance
This bar chart shows the importance of different features in predicting sales.

![Feature Importance](https://github.com/Fuatorium/Huawei/blob/main/sales_forecasting/graphs/Figure_2.png)

### Time Series Analysis
This line chart represents the total sales over time, highlighting trends and patterns.

![Time Series Analysis](https://github.com/Fuatorium/Huawei/blob/main/sales_forecasting/graphs/Figure_3.png)

### Sales by Store
This bar chart displays the total sales for each store.

![Sales by Store](https://github.com/Fuatorium/Huawei/blob/main/sales_forecasting/graphs/Figure_4.png)

### Sales by Year and Month
This line chart shows the monthly sales trends over different years.

![Sales by Year and Month](https://github.com/Fuatorium/Huawei/blob/main/sales_forecasting/graphs/Figure_5.png)

### CPI vs Sales
This scatter plot illustrates the relationship between the Consumer Price Index (CPI) and sales.

![CPI vs Sales](https://github.com/Fuatorium/Huawei/blob/main/sales_forecasting/graphs/Figure_6.png)

### Unemployment vs Sales
This scatter plot shows the relationship between the unemployment rate and sales.

![Unemployment vs Sales](https://github.com/Fuatorium/Huawei/blob/main/sales_forecasting/graphs/Figure_7.png)

## How to Run

1. Clone the repository:
    ```sh
    git clone https://github.com/Fuatorium/Huawei.git
    cd Huawei/sales_forecasting
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Run the data cleaning script:
    ```sh
    python src/data_preprocessing.py
    ```

5. Run the model training script:
    ```sh
    python src/model_training.py
    ```

6. Run the prediction script:
    ```sh
    python src/prediction.py
    ```

7. Generate visualizations:
    ```sh
    python src/visualization.py
    ```

8. View the generated visualizations in the `graphs` folder.


## Setup

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd sales_forecasting
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Run the data preprocessing script:
    ```sh
    python src/data_preprocessing.py
    ```

4. Train the model:
    ```sh
    python src/model_training.py
    ```

5. Make predictions:
    ```sh
    python src/prediction.py
    ```

6. Visualize the results:
    ```sh
    python src/visualization.py
    ```


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

This project was developed as part of a retail sales forecasting initiative. Special thanks to the data providers and the open-source community for their contributions.
