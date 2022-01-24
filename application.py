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
    {"date":"2020-01-01", "price":"200"},
    {"date":"2020-02-01", "price":"205"},
    {"date":"2020-03-01", "price":"190"},
    {"date":"2020-04-01", "price":"190"},
    {"date":"2020-05-01", "price":"190"},
    {"date":"2020-06-01", "price":"190"},
    {"date":"2020-07-01", "price":"190"},
    {"date":"2020-08-01", "price":"190"},
    {"date":"2020-09-01", "price":"190"},
    {"date":"2020-10-01", "price":"190"}
  ]}
  ethereum = {"name":"ethereum", "pricing_history":[
    {"date":"2020-01-01", "price":"100"},
    {"date":"2020-02-01", "price":"105"},
    {"date":"2020-03-01", "price":"190"},
    {"date":"2020-04-01", "price":"190"},
    {"date":"2020-05-01", "price":"190"},
    {"date":"2020-06-01", "price":"190"},
    {"date":"2020-07-01", "price":"190"},
    {"date":"2020-08-01", "price":"190"},
    {"date":"2020-09-01", "price":"190"},
    {"date":"2020-10-01", "price":"190"}
  ]}
  tether = {"name":"tether", "pricing_history":[
    {"date":"2020-01-01", "price":"50"},
    {"date":"2020-02-01", "price":"55"},
    {"date":"2020-03-01", "price":"190"},
    {"date":"2020-04-01", "price":"190"},
    {"date":"2020-05-01", "price":"190"},
    {"date":"2020-06-01", "price":"190"},
    {"date":"2020-07-01", "price":"190"},
    {"date":"2020-08-01", "price":"190"},
    {"date":"2020-09-01", "price":"190"},
    {"date":"2020-10-01", "price":"190"}
  ]}
  solana = {"name":"solana", "pricing_history":[
    {"date":"2020-01-01", "price":"50"},
    {"date":"2020-02-01", "price":"55"},
    {"date":"2020-03-01", "price":"190"},
    {"date":"2020-04-01", "price":"190"},
    {"date":"2020-05-01", "price":"190"},
    {"date":"2020-06-01", "price":"190"},
    {"date":"2020-07-01", "price":"190"},
    {"date":"2020-08-01", "price":"190"},
    {"date":"2020-09-01", "price":"190"},
    {"date":"2020-10-01", "price":"190"}
  ]}
  cardano = {"name":"cardano", "pricing_history":[
    {"date":"2020-01-01", "price":"50"},
    {"date":"2020-02-01", "price":"55"},
    {"date":"2020-03-01", "price":"190"},
    {"date":"2020-04-01", "price":"190"},
    {"date":"2020-05-01", "price":"190"},
    {"date":"2020-06-01", "price":"190"},
    {"date":"2020-07-01", "price":"190"},
    {"date":"2020-08-01", "price":"190"},
    {"date":"2020-09-01", "price":"190"},
    {"date":"2020-10-01", "price":"190"}
  ]}
  
  return json.dumps([bitcoin, ethereum, tether, solana, cardano])

from IPython.display import HTML
HTML("<a href='https://{}.{}'>Crypto Pricing App</a>".format(os.environ['CDSW_ENGINE_ID'],os.environ['CDSW_DOMAIN']))

if __name__=="__main__":
  app.run(port=int(os.environ['CDSW_APP_PORT']))