from alpaca.trading.client import TradingClient #gain access to account
from alpaca.data import StockHistoricalDataClient, StockTradesRequest
from datetime import datetime

#("user key", "secret key")
trading_client = TradingClient("PK13FWI2SQQ5H5RYLGRH","l1msaRjBwIVR4h1vNcTRxd2mtPfHqJvf42d3RMAI") #access account

print(trading_client.get_account().account_number)
print(trading_client.get_account().buying_power)


#("user key", "secret key")
data_client = StockHistoricalDataClient("PK13FWI2SQQ5H5RYLGRH","l1msaRjBwIVR4h1vNcTRxd2mtPfHqJvf42d3RMAI")

request_params = StockTradesRequest(
    symbol_or_symbols = "AAPL",
    start = datetime(2024, 1, 30, 14, 30), #(year,month,day,hour,min) UTC
    end = datetime(2024, 1, 30, 14, 45) #15 min later
)

trades = data_client.get_stock_trades(request_params) #make data request

for trade in trades.data["AAPL"]:
    print(trade)
    break
