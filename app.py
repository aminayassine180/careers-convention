#!/usr/bin/env python3

# local imports
from os import name
from os.path import abspath, dirname, join

import time
import logging
import sqlite3
from sqlite3 import Error

from flask import flash, Flask, Markup, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy



# create the flask application object
app = Flask(__name__)
app.config.from_object(__name__)

# create/connect to the db
_cwd = dirname(abspath(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + join(_cwd, 'flask-database.db')
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
def query_to_list(query, include_field_names=True):
    column_names = []
    for i, obj in enumerate(query.all()):
        if i == 0:
            column_names = [c.name for c in obj.__table__.columns]
            if include_field_names:
                yield column_names
        yield obj_to_list(obj, column_names)

def obj_to_list(sa_obj, field_order):
    return [getattr(sa_obj, field_name, None) for field_name in field_order]


# database models
class Category(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    internalurl = db.Column(db.String)

    def __repr__(self):
        return '<Category {:d} {}>'.format(self.id, self.name)

    def __str__(self):
        return self.name


class Delegate(db.Model):
    __tablename__ = 'delegate'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    location = db.Column(db.String)
    description = db.Column(db.String)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    internalurl = db.Column(db.String)
    externalurl = db.Column(db.String)

    def __repr__(self):
        return '<Delegate {:d} {}>'.format(self.id, self.name)

    def __str__(self):
        return self.name




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
  #TO DO - Add the ability to filter the list of delegates
  query = Delegate.query.filter(Delegate.id >= 0)

  return render_template('delegates.html', title='Delegates attending the Convention', description='', rows=query.all())

@app.route('/delegate/<string:internalURL>')
def get_delegate(internalURL):
  query = Delegate.query.filter_by(internalurl=internalURL).first_or_404()

  # In this instance, the meta title and description values must come from the database.
  return render_template('delegate.html', title='', description='', row=query)

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

# start the server with the 'run()' method - debug=True for testing - NOT LIVE
if __name__ == '__main__':
    app.debug = True
    db.create_all(app=app)
    db.init_app(app=app)
    app.run()
    #app.run(debug=True)
