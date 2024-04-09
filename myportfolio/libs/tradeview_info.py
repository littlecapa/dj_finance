from tradingview_ta import TA_Handler, Interval, Exchange
from .. import models
from datetime import datetime

class EXCEPTION_SymbolNotFound(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def save_search_history(symbol, screener="america", exchange="NASDAQ", interval=Interval.INTERVAL_1_DAY):
    try:
        handler = TA_Handler(
        symbol=symbol,
        screener=screener,
        exchange=exchange,
        interval=interval)

        analysis = handler.get_analysis()

        new_search = models.SearchHistory(
            symbol=symbol,
            sell=analysis.summary["SELL"],
            neutral=analysis.summary["NEUTRAL"],
            buy=analysis.summary["BUY"],
            price=analysis.indicators["close"],
            searched_at=datetime.now())

        new_search.save()

    except Exception as e:
        print(e)
        new_search = models.SearchHistory(
            symbol=symbol,
            sell=0,
            neutral=0,
            buy=0,
            price=-1.0,
            searched_at=datetime.now())

        new_search.save()

        raise EXCEPTION_SymbolNotFound(e)
