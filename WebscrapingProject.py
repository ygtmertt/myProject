import yfinance as yf
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

# Question 1: Extracting Tesla Stock Data Using yfinance
tesla_data = yf.download('TSLA', start='2021-01-01', end='2022-01-01')

# Display the first few rows of Tesla stock data
print("Tesla Stock Data:")
print(tesla_data.head())

# Question 2: Extracting Tesla Revenue Data Using Webscraping
tesla_url = "https://www.marketwatch.com/investing/stock/tsla/financials"
response = requests.get(tesla_url)
soup = BeautifulSoup(response.text, 'html.parser')
revenue = soup.find_all("td", {"class": "valueCell"})
tesla_revenue = revenue[0].text.strip()

print("\nTesla Revenue Data (Latest Quarter):", tesla_revenue)

# Question 3: Extracting GameStop Stock Data Using yfinance
gme_data = yf.download('GME', start='2021-01-01', end='2022-01-01')

# Display the first few rows of GameStop stock data
print("\nGameStop Stock Data:")
print(gme_data.head())

# Question 4: Extracting GameStop Revenue Data Using Webscraping
gme_url = "https://www.marketwatch.com/investing/stock/gme/financials"
response = requests.get(gme_url)
soup = BeautifulSoup(response.text, 'html.parser')
revenue = soup.find_all("td", {"class": "valueCell"})
gme_revenue = revenue[0].text.strip()

print("\nGameStop Revenue Data (Latest Quarter):", gme_revenue)

# Question 5: Tesla Stock and Revenue Dashboard
plt.figure(figsize=(10, 5))
plt.plot(tesla_data['Close'], label='Tesla Stock Price', color='blue')
plt.xlabel('Date')
plt.ylabel('Stock Price (USD)')
plt.title('Tesla Stock Price')
plt.legend()
plt.show()

# Question 6: GameStop Stock and Revenue Dashboard
plt.figure(figsize=(10, 5))
plt.plot(gme_data['Close'], label='GameStop Stock Price', color='red')
plt.xlabel('Date')
plt.ylabel('Stock Price (USD)')
plt.title('GameStop Stock Price')
plt.legend()
plt.show()
