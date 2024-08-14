from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetOrdersRequest
from alpaca.trading.enums import OrderSide, QueryOrderStatus

trading_client = TradingClient("PK13FWI2SQQ5H5RYLGRH","l1msaRjBwIVR4h1vNcTRxd2mtPfHqJvf42d3RMAI")

request_params = GetOrdersRequest(
    status = QueryOrderStatus.OPEN,
)

orders = trading_client.get_orders(request_params)
for order in orders: #cancel all orders
    trading_client.cancel_order_by_id(order.id)

