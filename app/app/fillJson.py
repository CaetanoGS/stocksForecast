import json
import yfinance as yf
from app import stockForecast

class JsonFill:
    def __init__(self, ticker, idate, fdate, perd):
        jsonFile = open("app//static//json//data.json")
        data = json.load(jsonFile)
        jsonFile.close()

        tickerData = yf.Ticker(ticker)

        if(perd == 'Daily'): pd = '1d'
        elif(perd == 'Weekly'): pd = '1wk'
        else: pd = '1mo'

        #get the historical prices for this ticker
        tickerDf = tickerData.history(interval=pd, start= idate, end=fdate)
        tickerDf.dropna(subset=['Open', 'High', 'Low', 'Close'])

        dfOpen = tickerDf['Open']
        dfHigh = tickerDf['High']
        dfLow = tickerDf['Low']
        dfClose = tickerDf['Close']

        Stocker = stockForecast.Stocker(ticker)

        data['Forecast']['Name'] = ticker
        data['Forecast']['LastOpen'] = dfOpen.iloc[-1]
        data['Forecast']['LastLow'] = dfLow.iloc[-1]
        data['Forecast']['LastHigh'] = dfHigh.iloc[-1]
        data['Forecast']['Change'] = "Sem valor"
        data['Forecast']['LastClose'] = dfClose.iloc[-1]
        data['Forecast']['TomorrowPrice'] = Stocker.value
        data['Forecast']['Error'] = Stocker.error

        #data['Forecast']['closeY'] = dfClose.values


        jsonFile = open("app//static//json//data.json", "w+")
        jsonFile.write(json.dumps(data))
        jsonFile.close()

        super().__init__()