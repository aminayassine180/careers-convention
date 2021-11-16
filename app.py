#!/usr/bin/env python3

# local imports
import time
import logging
from flask import Flask, render_template

# create the flask application object
app = Flask(__name__)

# Every page that is on the website will need an app.route defined here
@app.route('/')
def get_home():
  return render_template('home.html', title='Home')

@app.route('/about')
def get_about():
  return render_template('about.html')

@app.route('/acknowledgements')
def get_acknowledgements():
  return render_template('acknowledgements.html')

@app.route('/delegates')
def get_delegates():
  return render_template('delegates.html')

@app.route('/delegate/<url>')
def get_delegate(url):
  return "The passed URL is " + str(url)

@app.route('/feedback')
def get_feedback():
  return render_template('feedback.html')

@app.route('/map')
def get_map():
  return render_template('map.html')

@app.route('/news')
def get_news():
  return render_template('news.html')

# start the server with the 'run()' method - debug=True for testing - NOT LIVE
if __name__ == '__main__':
  app.run(debug=True)
