import yfinance 

tickers = ['AAPL', 'MSFT', 'AMZN']

stock_data = {}

for t in tickers:
    stock = yfinance.Ticker(t) #create ticker object

    historical_data = stock.history(period='1y') #1 year of market data

    #financial statements
    financials = stock.financials
    balance_sheet = stock.balance_sheet
    cashflow = stock.cashflow


    #store in dict
    stock_data[t] = {
        'historical_data': historical_data,
        'financials': financials,
        'balance_sheet': balance_sheet,
        'cashflow': cashflow
    }

print('AAPL Historical Data: ', stock_data['AAPL']['historical_data'].head(5))
print("0000000000000000000000000000000000")
print('AAPL Financials: ', stock_data['AAPL']['financials'])
print("0000000000000000000000000000000000")
print('AAPL Cash Flow: ', stock_data['AAPL']['cashflow'])
print("0000000000000000000000000000000000")
print('AAPL balance_sheet: ', stock_data['AAPL']['balance_sheet'])    