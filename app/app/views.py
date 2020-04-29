from app import app
from flask import render_template
from flask import jsonify
import yfinance as yf
from app import fillJson
import json



#from Foo.Project1 import file1

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    tickerSymbol = 'MSFT'

    #Stocker = stockForecast.Stocker(tickerSymbol)

    #print(Stocker.value, Stocker.error, Stocker.date)
    try:
        #value = Stocker.getTomorrowPrice(tickerSymbol)
        #print(value)
        return render_template('dashboard.html')
    except:
        print('Error')
        return render_template('dashboard.html')

    #get data on this ticker
    #tickerData = yf.Ticker(tickerSymbol)

    #get the historical prices for this ticker
    #tickerDf = tickerData.history(period='1d', start='2010-1-1', end='2020-1-25')

    #see your data
    #print(tickerDf.index)
    return render_template('dashboard.html')

@app.route('/JSON/<ticker>/<initialDate>/<finalDate>/<period>', methods=['GET'])
def getJSON(ticker, initialDate, finalDate, period):
    #print(ticker, initialDate, finalDate, period)

    df = fillJson.JsonFill(ticker, initialDate, finalDate, period)

    jsonFile = open("app//app//static//json//data.json")
    data = json.load(jsonFile)
    jsonFile.close()
    return jsonify(data)


    