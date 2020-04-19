from app import app
from flask import render_template
from app.stocks import Stocks
import yfinance as yf

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def about():
    tickerSymbol = 'MSFT'

    #get data on this ticker
    tickerData = yf.Ticker(tickerSymbol)

    #get the historical prices for this ticker
    tickerDf = tickerData.history(period='1d', start='2010-1-1', end='2020-1-25')

    #see your data
    #print(tickerDf.index)
    return render_template('dashboard.html')