# Iris Species Analysis and Modeling

This project performs a comprehensive analysis of the Iris species dataset, including various visualizations to understand the patterns, relationships, and classification of the species.

## Data Cleaning

The data cleaning process involves:
- Converting column names to lowercase.
- Removing any irrelevant data.
- Checking for missing values and handling them if necessary.

## Visualizations

### Pairplot of Iris Dataset
This pairplot visualizes the pairwise relationships between features colored by species.

![Pairplot](https://github.com/Fuatorium/Huawei/blob/main/Iris-Species/graphs/Figure_1.png)

### Sepal Length by Species
This boxplot shows the distribution of Sepal Length across different species.

![Sepal Length by Species](https://github.com/Fuatorium/Huawei/blob/main/Iris-Species/graphs/Figure_2.png)

### Sepal Width by Species
This boxplot shows the distribution of Sepal Width across different species.

![Sepal Width by Species](https://github.com/Fuatorium/Huawei/blob/main/Iris-Species/graphs/Figure_3.png)

### Petal Length by Species
This boxplot shows the distribution of Petal Length across different species.

![Petal Length by Species](https://github.com/Fuatorium/Huawei/blob/main/Iris-Species/graphs/Figure_4.png)

### Petal Width by Species
This boxplot shows the distribution of Petal Width across different species.

![Petal Width by Species](https://github.com/Fuatorium/Huawei/blob/main/Iris-Species/graphs/Figure_5.png)

### Correlation Matrix
This heatmap displays the correlation between different features in the dataset.

![Correlation Matrix](https://github.com/Fuatorium/Huawei/blob/main/Iris-Species/graphs/Figure_6.png)

### Feature Importance
This bar chart shows the importance of each feature in the classification model.

![Feature Importance](https://github.com/Fuatorium/Huawei/blob/main/Iris-Species/graphs/Figure_7.png)

## Conclusion

This analysis provides insights into the patterns and relationships between different features of the Iris dataset. The visualizations help in identifying key trends and the most significant contributors to the classification model.

## How to Run

1. Clone the repository:
    ```bash
    git clone https://github.com/Fuatorium/Huawei
    cd Huawei/Iris-Species
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the data cleaning and analysis script:
    ```bash
    python scripts/data_cleaning.py
    ```

4. View the generated visualizations in the `graphs` folder.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
