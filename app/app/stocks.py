import yfinance as yf


class Stocks:
    def __init__(self):
        pass

    def getStock(self, stockName, period, beginData, endDate):
        tickerData = yf.Ticker(stockName)

        # get the historical prices for this ticker
        tickerDf = tickerData.history(period, beginData='2010-1-1', endDate='2020-1-25')

        # see your data
        print(tickerDf)
        return tickerDf
