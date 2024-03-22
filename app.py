import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
from pmdarima import auto_arima

# Fetch the last day's data for AAPL
ticker = yf.Ticker("AAPL")
last_day_data = ticker.history(period='1d')

# Extract the closing price for the last day
previous_day_closing_price = last_day_data['Close'][0]

# Load data
stocks = pd.read_csv('apple_preprocessed.csv')

# Drop the 'Date' column from both features and target
X = stocks.drop(['Close', 'Date'], axis=1)
y = stocks['Close']

# Split data
split = 0.3
train_split = int(split * len(X))
X_train, y_train = X[:train_split], y[:train_split]
X_test, y_test = X[train_split:], y[train_split:]

# Create an Auto ARIMA model
auto_model = auto_arima(y_train, trace=True, error_action='ignore', suppress_warnings=True)

# Fit the model to the training data
auto_model.fit(y_train)

# Fetch real-time stock data
ticker = 'AAPL' # Apple Inc.
stock_data = yf.download(ticker, start='2020-01-01', end='2024-03-22')

# Prepare the data for prediction
# Assuming the model requires the same features as the training data
# For simplicity, we'll use the last 10 days of data as an example
last_10_days = stock_data.tail(10)
last_10_days = last_10_days.reset_index()
X_real_time = last_10_days.drop(['Close', 'Date', 'Adj Close'], axis=1)

# Predict the closing price
y_pred = auto_model.predict(n_periods=1)

# Streamlit app
st.title("Stock Price Prediction with Auto ARIMA")

st.write("Previous Day's Closing Price:", previous_day_closing_price)
st.write("Predicted Closing Price: ", y_pred)

# Plotting predictions vs actual values
plt.figure(figsize=(10, 6))
plt.plot(y_test, label='Actual')
plt.plot(y_pred, label='Predicted')
plt.xlabel('Time')
plt.ylabel('Stock Price')
plt.legend()
st.pyplot(plt.gcf())
