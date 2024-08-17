from alpaca.data.live import StockDataStream

stream = StockDataStream("","")

async def handle_trade(data):
    print(data)

stream.subscribe_trades(handle_trade, ["array of symbols"])

stream.run() #get live trade updates