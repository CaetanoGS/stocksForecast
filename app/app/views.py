from app import app
from flask import render_template, request
from flask import jsonify
import yfinance as yf
from app import fillJson
import json
from datetime import datetime



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

        fdate_datetime = datetime.strptime(final_date,'%Y-%m-%d')
        idate_datetime = datetime.strptime(initial_date, '%Y-%m-%d')

        if(fdate_datetime < idate_datetime):
            aux = final_date
            final_date = initial_date
            initial_date = aux
            aux = fdate_datetime
            fdate_datetime = idate_datetime
            idate_datetime = aux
        
        dif = fdate_datetime - idate_datetime



        if(period_select == 'Daily'):
            op1 = 'Selected'
            op2 = ''
            op3 = ''
        elif(period_select == 'Weekly'):
            if(dif.days <= 5):
                op1 = 'Selected'
                op2 = ''
                op3 = ''
            else:
                op1 = ''
                op2 = 'Selected'
                op3 = ''
        else:
            if(dif.days <= 5):
                op1 = 'Selected'
                op2 = ''
                op3 = ''
            elif (dif.days < 20):
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


    