from app import app
from flask import render_template
import yfinance as yf
from app import stockForecast



#from Foo.Project1 import file1

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    tickerSymbol = 'MSFT'

    Stocker = stockForecast.Stocker(tickerSymbol)

    print(Stocker.value, Stocker.error, Stocker.date)
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

@app.route('/forecast')
def forecast():
    tickerSymbol = 'MSFT'

    Stocker = stockForecast.Stocker(tickerSymbol)

    print(Stocker.value, Stocker.error, Stocker.date)
 
    return render_template('forecast.html')
    