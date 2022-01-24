import json
import logging
import os
from flask import Flask, render_template

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)

@app.route('/')
def home():
  return render_template("home.html")

@app.route('/sample_data')
def sample_data():
  bitcoin = {"name":"bitcoin", "pricing_history":[
    {"date":"2020-01-01", "price":"100"},
    {"date":"2020-02-01", "price":"105"},
    {"date":"2020-03-01", "price":"90"}
  ]}
  ethereum = {"name":"ethereum", "pricing_history":[
    {"date":"2020-01-01", "price":"100"},
    {"date":"2020-02-01", "price":"105"},
    {"date":"2020-03-01", "price":"90"}
  ]}
  tether = {"name":"tether", "pricing_history":[
    {"date":"2020-01-01", "price":"100"},
    {"date":"2020-02-01", "price":"105"},
    {"date":"2020-03-01", "price":"90"}
  ]}
  
  return json.dumps([bitcoin, ethereum, tether])

from IPython.display import HTML
HTML("<a href='https://{}.{}'>Crypto Pricing App</a>".format(os.environ['CDSW_ENGINE_ID'],os.environ['CDSW_DOMAIN']))

if __name__=="__main__":
  app.run(port=int(os.environ['CDSW_APP_PORT']))