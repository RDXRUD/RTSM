import time, datetime
from ibapi.client import EClient
from ibapi.wrapper import EWrapper

from ibapi.client import Contract

from lightweight_charts import Chart

from threading import Thread


INITIAL_SYMBOL = "TSM"

DEFAULT_HOST = '127.0.0.1'
DEFAULT_CLIENT_ID = 1

LIVE_TRADING = False
LIVE_TRADING_PORT = 7496
PAPER_TRADING_PORT = 7497
TRADING_PORT = PAPER_TRADING_PORT
if LIVE_TRADING:
    TRADING_PORT = LIVE_TRADING_PORT


class IBClient(EWrapper, EClient):
     
    def __init__(self, host, port, client_id):
        EClient.__init__(self, self) 
        
        self.connect(host, port, client_id)

        thread = Thread(target=self.run)
        thread.start()


    def error(self, req_id, code, msg, misc):
        if code in [2104, 2106, 2158]:
            print(msg)
        else:
            print('Error {}: {}'.format(code, msg))


    def historicalData(self, req_id, bar):
        print(bar)


    # callback when all historical data has been received
    def historicalDataEnd(self, reqId, start, end):
        print(f"end of data {start} {end}")


def get_bar_data(symbol, timeframe):
    print(f"getting bar data for {symbol} {timeframe}")

    contract = Contract()
    contract.symbol = symbol
    contract.secType = 'STK'
    contract.exchange = 'SMART'
    contract.currency = 'USD'
    what_to_show = 'TRADES'

    client.reqHistoricalData(
        2, contract, '', '30 D', timeframe, what_to_show, True, 2, False, []
    )

    time.sleep(1)
       
    chart.watermark(symbol)


if __name__ == '__main__':
    client = IBClient(DEFAULT_HOST, TRADING_PORT, DEFAULT_CLIENT_ID)
    time.sleep(1)

    chart = Chart(toolbox=True, width=1000, inner_width=0.6, inner_height=1)

    get_bar_data(INITIAL_SYMBOL, '5 mins')

    chart.show(block=True)