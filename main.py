"""`main` is the top level module for your Flask application."""

# Imports
import os
import jinja2
import webapp2
import logging
import json
import urllib

# this is used for constructing URLs to google's APIS
from googleapiclient.discovery import build

# Import the Flask Framework
from flask import Flask
app = Flask(__name__)

# This uses discovery to create an object that can talk to the 
# fusion tables API using the developer key
API_KEY = 'AIzaSyAFyXhIDS46k17aFMNTb5Hea3Yp2xPOEts'
service = build('fusiontables', 'v1', developerKey=API_KEY)

TABLE_ID = '18TiFfCHF2WMxWazJFiNkUT5JHDy3Al3hp-fnvjPj'

request = service.column().list(tableId=TABLE_ID)

def get_all_data(self):
    query = "SELECT * FROM " + TABLE_ID + " WHERE  Scorer = 'Forlan' LIMIT 5"
    response = service.query().sql(sql=query).execute()
    logging.info(response['columns'])
    logging.info(response['rows'])
        
    return response


# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500
