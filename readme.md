# COVID-19 Data Analysis

This project analyzes the COVID-19 data to visualize the trend of confirmed cases, deaths, and recoveries over time globally.

![COVID-19 Data Analysis](path/to/your/image.png)

## Project Structure

- `data/`: Contains the raw and cleaned data files.
- `notebooks/`: Jupyter notebooks for interactive data analysis.
- `scripts/`: Python scripts for data cleaning, analysis, and visualization.
- `README.md`: Project documentation.
- `requirements.txt`: List of Python dependencies.

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/Fuatorium/Huawei.git
    cd Huawei/COVID-19-Data-Analysis
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Download the data files:
    ```bash
    python data_download.py
    ```

4. Run the data cleaning script:
    ```bash
    python scripts/data_cleaning.py
    ```

5. Run the data analysis script:
    ```bash
    python scripts/data_analysis.py
    ```

6. Run the data visualization script:
    ```bash
    python scripts/data_visualization.py
    ```

## Scripts

### data_download.py
Downloads the latest COVID-19 data from the Johns Hopkins University repository.

### data_cleaning.py
Cleans the raw data by melting the dataframes and formatting the dates.

### data_analysis.py
Analyzes the cleaned data and creates a summary CSV file with total confirmed cases, deaths, and recoveries over time.

### data_visualization.py
Visualizes the analysis results using Matplotlib and Plotly.

## Results

The analysis results and visualizations will be generated and displayed as specified in the scripts.

## License

This project is licensed under the MIT License.
