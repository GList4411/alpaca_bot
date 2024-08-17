import yfinance 
import numpy
import matplotlib.pyplot as plt

tickers = ['AAPL', 'MSFT', 'AMZN']

stock_data = {}

for t in tickers:
    stock = yfinance.Ticker(t) #create ticker object

    historical_data = stock.history(period='1y') #1 year of market data

    hist_np = {
        'Open': historical_data['Open'].values,
        'High': historical_data['High'].values,
        'Low': historical_data['Low'].values,
        'Close': historical_data['Close'].values,
        'Volume': historical_data['Volume'].values
    }

    #financial statements
    financials = stock.financials.values
    balance_sheet = stock.balance_sheet.values
    cashflow = stock.cashflow.values


    #store in dict
    stock_data[t] = {
        'historical_data': hist_np,
        'financials': financials,
        'balance_sheet': balance_sheet,
        'cashflow': cashflow
    }

    # Plot historical prices
    plt.figure(figsize=(12, 6))
    plt.plot(historical_data.index, historical_data['Close'], label=t)
    plt.title(f'{t} Historical Prices')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    # Display the plot
    plt.show()


'''
print('AAPL Historical Data: ', stock_data['AAPL']['historical_data'].head(5))
print("0000000000000000000000000000000000")
print('AAPL Financials: ', stock_data['AAPL']['financials'])
print("0000000000000000000000000000000000")
print('AAPL Cash Flow: ', stock_data['AAPL']['cashflow'])
print("0000000000000000000000000000000000")
print('AAPL balance_sheet: ', stock_data['AAPL']['balance_sheet'])    
'''