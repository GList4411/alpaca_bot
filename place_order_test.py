from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest, LimitOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

trading_client = TradingClient("PK13FWI2SQQ5H5RYLGRH","l1msaRjBwIVR4h1vNcTRxd2mtPfHqJvf42d3RMAI")

market_order_data = MarketOrderRequest(
    symbol = "AAPL",
    qty = 1,
    side = OrderSide.BUY,
    time_in_force = TimeInForce.DAY
)

market_order = trading_client.submit_order(market_order_data) #place a market order
print(market_order)

limit_order_data = LimitOrderRequest(
    symbol = "AAPL",
    qty = 1,
    side = OrderSide.BUY,
    time_in_force = TimeInForce.DAY,
    limit_price = 400.00
)

limit_order = trading_client.submit_order(limit_order_data) #place order with limit
print(limit_order)

positions = trading_client.get_all_positions()
print(positions) #display array of positions
for p in positions:
    print(p.symbol, p.current_price)