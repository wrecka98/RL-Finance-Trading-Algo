import yfinance as yf
import matplotlib.pyplot as plt

# Get stock data
data = yf.download("SHEL", start="2018-01-01", end="2020-01-01")
data.to_pickle("SHELL.pkl")

# Plot closing prices
plt.figure(figsize=(12, 6))
plt.plot(data['Close'], label='SHELL Closing Price', color='blue')
plt.title('SHELL Stock Price')
plt.xlabel('Date')
plt.ylabel('Price ($)')
plt.legend()
plt.grid(True)
plt.show()