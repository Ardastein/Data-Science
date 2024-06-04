# E-commerce Sales Analysis

This project performs a comprehensive analysis of e-commerce sales data, including various visualizations to understand the sales patterns, revenue distribution, and product popularity.

## Data Cleaning

The data cleaning process involves:
- Converting date columns to datetime format.
- Calculating total revenue for each transaction.
- Handling missing values and removing any irrelevant data.

## Visualizations

### Top 10 Countries by Quantity Sold
This bar chart shows the top 10 countries with the highest quantity of products sold.

![Top 10 Countries by Quantity Sold](https://github.com/Fuatorium/Huawei/blob/main/E-commerce-Sales-Analysis/graphs/Figure_2.png)

### Monthly Sales
This line chart represents the total quantity of products sold each month.

![Monthly Sales](https://github.com/Fuatorium/Huawei/blob/main/E-commerce-Sales-Analysis/graphs/Figure_3.png)

### Top 10 Products by Quantity Sold
This bar chart displays the top 10 most sold products.

![Top 10 Products by Quantity Sold](https://github.com/Fuatorium/Huawei/blob/main/E-commerce-Sales-Analysis/graphs/Figure_4.png)

### Revenue by Country (Top 5)
This pie chart shows the revenue distribution among the top 5 countries.

![Revenue by Country (Top 5)](https://github.com/Fuatorium/Huawei/blob/main/E-commerce-Sales-Analysis/graphs/Figure_5.png)

### Monthly Revenue
This line chart represents the total revenue generated each month.

![Monthly Revenue](https://github.com/Fuatorium/Huawei/blob/main/E-commerce-Sales-Analysis/graphs/Figure_6.png)

### Top 10 Products by Revenue
This bar chart displays the top 10 products that generated the most revenue.

![Top 10 Products by Revenue](https://github.com/Fuatorium/Huawei/blob/main/E-commerce-Sales-Analysis/graphs/Figure_7.png)

### Top 10 Invoices by Quantity
This bar chart shows the top 10 invoices with the highest quantity of products sold.

![Top 10 Invoices by Quantity](https://github.com/Fuatorium/Huawei/blob/main/E-commerce-Sales-Analysis/graphs/Figure_8.png)

### Top 10 Invoices by Revenue
This bar chart displays the top 10 invoices that generated the most revenue.

![Top 10 Invoices by Revenue](https://github.com/Fuatorium/Huawei/blob/main/E-commerce-Sales-Analysis/graphs/Figure_9.png)

## Conclusion

This analysis provides insights into the sales patterns, revenue distribution, and product popularity in the e-commerce dataset. The visualizations help in identifying the key trends and the most significant contributors to the business.

## How to Run

1. Clone the repository:
    ```bash
    git clone https://github.com/Fuatorium/Huawei
    cd Huawei/E-commerce-Sales-Analysis
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
