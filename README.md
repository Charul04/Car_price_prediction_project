##🚗 Car Price Prediction using Machine Learning

##📌 Project Overview

This project focuses on building an end-to-end Machine Learning pipeline to predict car prices based on multiple numerical and categorical features. The goal of the project is not only to train a model, but also to understand data limitations, preprocessing challenges, model evaluation, and deployment.

The project includes:

Data analysis and preprocessing

Feature engineering

Model training and evaluation

Model deployment using Streamlit

## 🧠 Problem Statement

Predict the Price of a Car (USD) based on features such as:

Brand

Manufacture Year

Engine Capacity

Horsepower

Mileage

Fuel Type

Transmission

Manufacturing Country

Car Age

Efficiency-related features

## 🗂 Dataset Description

Total rows: 300

Features include both numerical and categorical variables

Target variable: Price_USD

Feature Types

Numerical:
Manufacture_Year, Engine_CC, Horsepower, Mileage_km_per_l, Car_Age, HP_per_CC, Efficiency_Score

Categorical:
Brand, Fuel_Type, Body_Type, Transmission, Manufacturing_Country

Some non-predictive columns such as Car_ID, Age_Category, and Price_Category were removed during preprocessing.

## ⚙️ Technologies & Tools Used

Programming Language: Python

Libraries:

NumPy

Pandas

Matplotlib

Seaborn

scikit-learn

Models:

Linear Regression

Random Forest Regressor

Deployment: Streamlit

Model Saving: joblib

## 🔄 Machine Learning Pipeline

To ensure consistency between training and deployment, a pipeline was used:

Data Cleaning & EDA

Feature Selection

Splitting Numerical and Categorical Features

Preprocessing using ColumnTransformer

StandardScaler for numerical features

OneHotEncoder for categorical features

Model Training

Evaluation using MAE, MSE, and R²

Model Serialization

Streamlit Web App for Prediction

## 📊 Model Evaluation

During experimentation, the models showed:

Reasonable error values (MAE, MSE)

Low or negative R² score

Key Learning:

The model often predicted values close to the median car price, indicating that:

The dataset has weak feature–target correlation

Model performance is limited by data quality, not algorithm choice

This project helped highlight the importance of:

Target distribution

Baseline comparison

Data signal vs model complexity

## 🌐 Streamlit Web Application

A simple Streamlit app was built to:

Take user inputs for car features

Load the trained ML pipeline

Predict car prices in real time

This helped in understanding deployment challenges, such as:

Schema consistency

Handling categorical features

Passing inputs as DataFrames instead of NumPy arrays

## 📚 Key Learnings

Data quality is more important than model complexity

Poor R² does not always mean poor modeling

Pipelines are essential for real-world ML systems

Deployment exposes issues that training alone does not

Failure analysis is a critical ML skill

## 🚀 Future Improvements

Use a larger, higher-quality dataset

Add more influential features (market demand, car condition, ownership history)

Perform hyperparameter tuning

Try advanced models like Gradient Boosting or XGBoost

Improve UI and validation in Streamlit app
