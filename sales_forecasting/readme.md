# Sales Forecasting Project

This project aims to build a sales forecasting model using historical sales data.

## Project Structure
sales_forecasting/
├── data/
│ ├── features.csv
│ ├── stores.csv
│ ├── train.csv
│ ├── test.csv
├── src/
│ ├── data_preprocessing.py
│ ├── model_training.py
│ ├── prediction.py
│ ├── visualization.py
├── output/
│ ├── submission.csv
├── README.md
├── requirements.txt

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

## Data
The data used in this project consists of four CSV files:
- `features.csv`
- `stores.csv`
- `train.csv`
- `test.csv`

## Model
The model used for sales forecasting is a Random Forest Regressor.

## Visualization
The results are visualized using matplotlib.

