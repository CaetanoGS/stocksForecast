# Necessary imports

import json
import yfinance as yf
import numpy
from app import stockForecast



class JsonFill:
    def __init__(self, ticker, idate, fdate, perd):

        # Open the default JSON

        jsonFile = open("app//static//json//data.json")
        data = json.load(jsonFile)
        jsonFile.close()

        # Get the stock

        tickerData = yf.Ticker(ticker)

        # Front end inputs control

        if(perd == 'Daily'): pd = '1d'
        elif(perd == 'Weekly'): pd = '1wk'
        else: pd = '1mo'

        #get the historical prices for this ticker

        tickerDf = tickerData.history(interval=pd, start= idate, end=fdate)

        # Remove NaN values from the dataframe

        tickerDf = tickerDf.interpolate()

        # Create new dataframes to save the importants col for our application

        dfOpen = tickerDf['Open']
        dfHigh = tickerDf['High']
        dfLow = tickerDf['Low']
        dfClose = tickerDf['Close']

        # Converting numpy array in a simple list

        self.Open = dfOpen.values.tolist()
        self.High = dfHigh.values.tolist()
        self.Low = dfLow.values.tolist()
        self.Close = dfClose.values.tolist()

        self.date = numpy.datetime_as_string(tickerDf.index, unit='D')
        self.date = self.date.tolist()

        # Get the prediction value

        Stocker = stockForecast.Stocker(ticker)

        # Calculating the variation between the Close and Open of the last day searched by the user

        var = 100*((Stocker.value - dfClose.iloc[-1])/dfClose.iloc[-1])

        # Filling the JSON file up

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

        # Writing the JSON changes
        
        jsonFile = open("app//static//json//data.json", "w+")
        jsonFile.write(json.dumps(data))
        jsonFile.close()

        super().__init__()