import flask
from flask import Flask
from flask import json
from flask import jsonify, request
import datetime
import requests
from flask import render_template, redirect, url_for
import os
import sqlite3
from time import sleep
from sense_hat import SenseHat
sense = SenseHat()


app = Flask(__name__)

@app.route('/main')
def home():
   return render_template('main.html')
@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      reminder = request.form['r']
      form_date = request.form['date'] 

      form_time = request.form['time'] 


      date = datetime.datetime.strptime(form_date + " " + form_time,"%Y-%m-%d %H:%M")

      conn = sqlite3.connect('./static/data/info.db')
      curs = conn.cursor()
      curs.execute('INSERT INTO reminders (reminder,date) VALUES((?),(?))', (reminder,date))
      messages = []
      rows = curs.execute("SELECT * from reminders")
      for row in rows:
         message = {'reminder' : row[0],'id' : row[1], 'time' : row[2]}
         messages.append(message)
      conn.commit()
      conn.close()

      return render_template('index.html', messages = messages)
   else:

      reminder = request.args.get('r')

      form_date = request.args.get('date') 

      form_time = request.form.get('time') 

        
      date = datetime.datetime.strptime(form_date + " " + form_time,"%Y-%m-%d %H:%M")


      conn = sqlite3.connect('./static/data/info.db')
      curs = conn.cursor()
      curs.execute('INSERT INTO reminders (reminder,date) VALUES((?),(?))', (reminder,date))
      messages = []
      rows = curs.execute("SELECT * from reminders")
      for row in rows:
         message = {'reminder' : row[0],'id' : row[1],'time' : row[2]}
         messages.append(message)
      conn.commit()
      conn.close()


      return render_template('index.html', messages = messages)

@app.route('/', methods=['GET'])
def submit():
   conn = sqlite3.connect('./static/data/info.db')
   curs = conn.cursor()
   messages = []
   rows = curs.execute("SELECT * from reminders")
   for row in rows:
      message = {'reminder' : row[0],'id' : row[1],'time' : row[2]}
      messages.append(message)
   conn.close()
   return render_template('index.html', messages = messages)

@app.route('/buttonPressed/<btn>/<reminder>')
def delete_task(btn,reminder):
    conn = sqlite3.connect('./static/data/info.db')
    sql = 'DELETE FROM reminders WHERE id=?'
    curs = conn.cursor()
    curs.execute(sql, (btn,))
    messages = []
    rows = curs.execute("SELECT * from reminders")
    for row in rows:
      message = {'reminder' : row[0],'id' : row[1],'time' : row[2]}
      messages.append(message)

    conn.commit()
    conn.close()
    sense.show_message('You have completed ')
    sense.show_message(reminder)
    return render_template('index.html', messages = messages)

@app.route('/deleteAll')
def delete_all():
    conn = sqlite3.connect('./static/data/info.db')
    sql = 'DELETE FROM reminders'
    curs = conn.cursor()
    curs.execute(sql)
    messages = []
    rows = curs.execute("SELECT * from reminders")
    for row in rows:
      message = {'reminder' : row[0],'id' : row[1],'time' : row[2]}
      messages.append(message)
    conn.commit()
    conn.close()
    return render_template('index.html', messages = messages)






if __name__ == '__main__':
    app.run(debug = True, host='127.0.0.1')