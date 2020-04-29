import json
import yfinance as yf
from app import stockForecast
import numpy

class JsonFill:
    def __init__(self, ticker, idate, fdate, perd):
        jsonFile = open("app//app//static//json//data.json")
        data = json.load(jsonFile)
        jsonFile.close()

        tickerData = yf.Ticker(ticker)

        if(perd == 'Daily'): pd = '1d'
        elif(perd == 'Weekly'): pd = '1wk'
        else: pd = '1mo'

        #get the historical prices for this ticker
        tickerDf = tickerData.history(interval=pd, start= idate, end=fdate)
        tickerDf = tickerDf.dropna(subset=['Open', 'High', 'Low', 'Close'])

        dfOpen = tickerDf['Open']
        dfHigh = tickerDf['High']
        dfLow = tickerDf['Low']
        dfClose = tickerDf['Close']

        self.Open = dfOpen.values.tolist()
        self.High = dfHigh.values.tolist()
        self.Low = dfLow.values.tolist()
        self.Close = dfClose.values.tolist()

        self.date = numpy.datetime_as_string(tickerDf.index, unit='D')
        self.date = self.date.tolist()

        Stocker = stockForecast.Stocker(ticker)

        var = 100*((Stocker.value - dfClose.iloc[-1])/dfClose.iloc[-1])
        data['Forecast']['Name'] = ticker
        data['Forecast']['LastOpen'] = dfOpen.iloc[-1]
        data['Forecast']['LastLow'] = dfLow.iloc[-1]
        data['Forecast']['LastHigh'] = dfHigh.iloc[-1]
        data['Forecast']['Change'] = var
        data['Forecast']['LastClose'] = dfClose.iloc[-1]
        data['Forecast']['TomorrowPrice'] = Stocker.value
        data['Forecast']['Error'] = Stocker.error
        data['Forecast']['closeY'] = self.Close
        data['Forecast']['openY'] = self.Open
        data['Forecast']['lowY'] = self.Low
        data['Forecast']['highY'] = self.High
        data['Forecast']['dateX'] = self.date


        jsonFile = open("app//app//static//json//data.json", "w+")
        jsonFile.write(json.dumps(data))
        jsonFile.close()

        super().__init__()