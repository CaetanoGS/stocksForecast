from app import app
from flask import render_template, request
from flask import jsonify
import yfinance as yf
from app import fillJson
import json



#from Foo.Project1 import file1

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard', methods=['POST','GET'])
def dashboard():

    if(request.method == 'POST'):
        company_name = request.form['companyName']
        final_date = request.form['endDate']
        initial_date = request.form['beginDate']
        period_select = request.form['period']

        if(period_select == 'Daily'):
            op1 = 'Selected'
            op2 = ''
            op3 = ''
        elif(period_select == 'Weekly'):
            op1 = ''
            op2 = 'Selected'
            op3 = ''
        else:
            op1 = ''
            op2 = ''
            op3 = 'Selected'
            
        return render_template('dashboard.html', name= company_name, fdate= final_date, idate= initial_date, option1=op1, option2=op2, option3=op3)
    else:
        return render_template('dashboard.html', name='SPY', fdate= '2020-04-29', idate = '2018-12-01', option1='Selected', option2='', option3='')

@app.route('/JSON/<ticker>/<initialDate>/<finalDate>/<period>', methods=['GET'])
def getJSON(ticker, initialDate, finalDate, period):
    #print(ticker, initialDate, finalDate, period)

    df = fillJson.JsonFill(ticker, initialDate, finalDate, period)

    jsonFile = open("app//app//static//json//data.json")
    data = json.load(jsonFile)
    jsonFile.close()
    return jsonify(data)


    