# Netflix Reviews Sentiment Analysis

This project performs sentiment analysis on Netflix reviews. The analysis includes preprocessing the text data, building a sentiment classification model using logistic regression, and visualizing the results.

## Table of Contents

- [Introduction](#introduction)
- [Data](#data)
- [Data Preprocessing](#data-preprocessing)
- [Modeling](#modeling)
- [Evaluation](#evaluation)
- [Visualizations](#visualizations)
- [How to Run](#how-to-run)
- [Conclusion](#conclusion)

## Introduction

Sentiment analysis is a key component in understanding customer opinions and feedback. This project aims to classify Netflix reviews as either positive or negative based on the sentiment expressed in the review content.

## Data

The dataset used in this project contains Netflix reviews. The main columns used for the analysis are:
- `content`: The text of the review.
- `score`: The rating given by the reviewer.

## Data Preprocessing

Before building the model, the data needs to be preprocessed. This includes:
1. Lowercasing the text.
2. Removing punctuation.
3. Splitting the data into training and testing sets.

## Modeling

A logistic regression model is used for sentiment classification. The text data is vectorized using the Bag of Words approach.

## Evaluation

The model's performance is evaluated using accuracy, confusion matrix, and classification report.

## Visualizations

### Word Cloud for Positive Reviews
![Word Cloud Positive](https://github.com/Fuatorium/Huawei-Speed-Run/blob/main/Netflix-Reviews/visualizations/wordcloud_positive.png)

### Model Accuracy Comparison
![Model Accuracy Comparison](https://github.com/Fuatorium/Huawei-Speed-Run/blob/main/Netflix-Reviews/visualizations/Figure_1.png)

### Confusion Matrix
![Confusion Matrix](https://github.com/Fuatorium/Huawei-Speed-Run/blob/main/Netflix-Reviews/visualizations/Figure_2.png)

### Classification Report
![Classification Report](https://github.com/Fuatorium/Huawei-Speed-Run/blob/main/Netflix-Reviews/visualizations/Figure_3.png)

## How to Run

1. Clone the repository:
    ```bash
    git clone https://github.com/Fuatorium/Huawei-Speed-Run
    cd Huawei-Speed-Run/Netflix-Reviews
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the analysis script:
    ```bash
    python Netflix.py
    ```

## Conclusion

This project demonstrates how to perform sentiment analysis on text data using logistic regression. The model achieves a reasonable accuracy and the visualizations provide insights into the model's performance.

Feel free to explore the repository and use the code for your own sentiment analysis projects.
