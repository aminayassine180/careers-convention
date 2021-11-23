#!/usr/bin/env python3

# local imports
import time
import logging
import sqlite3
from sqlite3 import Error

from flask import Flask, render_template

# create the flask application object
app = Flask(__name__)


# Every page that is on the website will need an app.route defined here
@app.route('/')
def get_home():
  return render_template('home.html', title='Home', description='This is the meta-description.')

@app.route('/about')
def get_about():
  return render_template('about.html', title='More about our Convention', description='')

@app.route('/acknowledgements')
def get_acknowledgements():
  return render_template('acknowledgements.html', title='Acknowledgements of the Convention', description='')

@app.route('/delegates')
def get_delegates():
  strSQL = "SELECT * FROM delegates ORDER BY name ASC"

  # open conntection to the database
  dbConnection = sqlite3.connect("database.db")

  #Setup a cursor using the current DB connection
  dbConnection.row_factory = sqlite3.Row
  cur = dbConnection.cursor()
  cur.execute(strSQL)

  #Get all of the rows, passing them to the template
  rows = cur.fetchall(); 

  return render_template('delegates.html', title='Delegates attending the Convention', description='', rows=rows)

@app.route('/delegate/<string:internalURL>')
def get_delegate(internalURL):
  strSQL = "SELECT * FROM delegates WHERE internalURL = '" + internalURL + "'"

  # open conntection to the database
  dbConnection = sqlite3.connect("database.db")

  #Setup a cursor using the current DB connection
  dbConnection.row_factory = sqlite3.Row
  cur = dbConnection.cursor()
  cur.execute(strSQL)

  #Get all of the rows, passing them to the template
  row = cur.fetchone()


  # In this instane, the meta title and description values must come from the database.
  return render_template('delegate.html', internalURL=internalURL, title='', description='', row=row)

@app.route('/feedback')
def get_feedback():
  #TO DO - Create the form itself.
  #TO DO - Create a new route to send the form contents to the database.

  return render_template('feedback.html', title='Feedback Form', description='')

@app.route('/map')
def get_map():
  return render_template('map.html', title='Location Map of the Convention', description='')

@app.route('/news')
def get_news():
  return render_template('news.html', title='Latest news from the Careers Convention', description='')

@app.errorhandler(404)
def page_not_found(error):
   return render_template('error404.html', title = 'Page not found'), 404

#@app.teardown_appcontext
#def closeDB():
#  dbConnection.close
#  return True

# start the server with the 'run()' method - debug=True for testing - NOT LIVE
if __name__ == '__main__':
  app.run(debug=True)
