import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import math as mt

# Load data
stocks = pd.read_csv('apple_preprocessed.csv')
X = stocks.drop(['Close', 'Date'], axis=1)
y = stocks['Close']

# Split data
split = 0.3
train_split = int(split * len(X))
X_train, y_train = X[:train_split], y[:train_split]
X_test, y_test = X[train_split:], y[train_split:]

# Create a Linear Regression model
linreg_model = LinearRegression()

# Fit the model to the training data
linreg_model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = linreg_model.predict(X_test)

# Calculate model performance metrics
mse = mean_squared_error(y_test, y_pred)
rmse = mt.sqrt(mse)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Streamlit app
st.title("Stock Price Prediction with Linear Regression")

st.write("Mean Squared Error (MSE): ", mse)
st.write("Root Mean Squared Error (RMSE): ", rmse)
st.write("Mean Absolute Error (MAE): ", mae)
st.write("R-squared (R2): ", r2)

# Plotting predictions vs actual values
plt.figure(figsize=(10, 6))
plt.plot(y_test, label='Actual')
plt.plot(y_pred, label='Predicted')
plt.xlabel('Time')
plt.ylabel('Stock Price')
plt.legend()
st.pyplot(plt.gcf())