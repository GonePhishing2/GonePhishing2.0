# GonePhishing2.0
 USU Hackathon Project
# AI & Machine Learning Project: Parts Delivery Prediction

Welcome to our AI & Machine Learning project repository! This project was completed as part of a hackathon organized by Utah State University, focusing on the Snowflake data platform. We were tasked with predicting the arrival time of spare parts for a manufacturing company, aiming to address delays in part deliveries.

## Project Overview

Our primary objective was to leverage AI and machine learning techniques to improve the accuracy of part delivery predictions. This involved a comprehensive approach from data cleaning to model selection, with the ultimate goal of providing our stakeholders with a reliable forecasting tool.

## Problem Statement

The challenge we faced revolved around the uncertainty in predicting delivery times due to disorganized data. Our task was to streamline this data to enhance the effectiveness of our machine learning models. By doing so, we aimed to improve operational efficiency and minimize production delays.

## Data Cleaning and Preparation

### Dealing with Data Types
We began by addressing inconsistencies in data types, particularly converting numeric date values to the appropriate date format.

### Handling Null Values
To ensure data integrity, we filled in missing values where possible and removed rows with null values in specific columns.

### Creating New Columns
We introduced new columns to aid in our analysis, such as determining whether a delivery was late or not.

## Model Feature Engineering

Our analytical model focused on predicting delivery performance by examining the lag between planned and actual delivery dates. Key engineered features were created to capture crucial aspects of supply chain management, such as timeliness of delivery.

## Modeling Techniques

### Binary Classification
We initiated our modeling process with a basic binary classification approach to categorize deliveries as early or late.

### Regression with PyCaret
Continuing from the binary classification, we performed regression analysis to assess model performance on continuous data, providing foundational insights for subsequent techniques.

### Classification with PyCaret
Moving beyond binary classification, we categorized deliveries into discrete time intervals to gain a more detailed understanding of delivery times.

### Tuning with PyCaret
To optimize model performance, we fine-tuned the best-performing model, focusing on binary classification due to memory constraints.

### Regression Neural Network
We explored the capabilities of a Neural Network for regression to provide more continuous predictions of delivery times, albeit with some optimization challenges.

### Neural Network Classification
Inspired by our initial classification models, we delved into Neural Network classification to further enhance predictive accuracy.

## Conclusion

Through collaborative effort and rigorous experimentation, we aimed to provide Koch Industries with an advanced predictive model for parts delivery. While challenges were encountered, we believe our efforts lay the foundation for future improvements and innovations in supply chain forecasting.

Thank you for visiting our repository! For more details, please explore our code and documentation.
