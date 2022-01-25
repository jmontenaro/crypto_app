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
  bitcoin = {"name":"Bitcoin", "pricing_history":[
    {"date":"2022-01-16","price":"43079.1"},
    {"date":"2022-01-17","price":"42209.3"},
    {"date":"2022-01-18","price":"42364.6"},
    {"date":"2022-01-19","price":"41677.8"},
    {"date":"2022-01-20","price":"40715.9"},
    {"date":"2022-01-21","price":"36475.5"},
    {"date":"2022-01-22","price":"35075.2"},
    {"date":"2022-01-23","price":"36269.5"},
    {"date":"2022-01-24","price":"36686.3"},
    {"date":"2022-01-25","price":"36826.2"}
  ]}
  ethereum = {"name":"Ethereum", "pricing_history":[
    {"date":"2022-01-16","price":"3346.59"},
    {"date":"2022-01-17","price":"3209.35"},
    {"date":"2022-01-18","price":"3160.15"},
    {"date":"2022-01-19","price":"3083.65"},
    {"date":"2022-01-20","price":"3004.72"},
    {"date":"2022-01-21","price":"2571.29"},
    {"date":"2022-01-22","price":"2412.52"},
    {"date":"2022-01-23","price":"2540.81"},
    {"date":"2022-01-24","price":"2441.01"},
    {"date":"2022-01-25","price":"2447.43"}
  ]}
  tether = {"name":"Tether", "pricing_history":[
    {"date":"2022-01-16","price":"1.0003"},
    {"date":"2022-01-17","price":"1.0003"},
    {"date":"2022-01-18","price":"1.0002"},
    {"date":"2022-01-19","price":"1.0003"},
    {"date":"2022-01-20","price":"1.0001"},
    {"date":"2022-01-21","price":"1.0004"},
    {"date":"2022-01-22","price":"1.0004"},
    {"date":"2022-01-23","price":"1.0006"},
    {"date":"2022-01-24","price":"1.0005"},
    {"date":"2022-01-25","price":"1.0006"}
  ]}
  solana = {"name":"Solana", "pricing_history":[
    {"date":"2022-01-16","price":"147.954"},
    {"date":"2022-01-17","price":"139.824"},
    {"date":"2022-01-18","price":"141.282"},
    {"date":"2022-01-19","price":"135.276"},
    {"date":"2022-01-20","price":"127.672"},
    {"date":"2022-01-21","price":"112.362"},
    {"date":"2022-01-22","price":"94.665"},
    {"date":"2022-01-23","price":"99.766"},
    {"date":"2022-01-24","price":"91.784"},
    {"date":"2022-01-25","price":"93.996"}
  ]}
  cardano = {"name":"Cardano", "pricing_history":[
    {"date":"2022-01-16","price":"1.4109"},
    {"date":"2022-01-17","price":"1.6015"},
    {"date":"2022-01-18","price":"1.4582"},
    {"date":"2022-01-19","price":"1.3368"},
    {"date":"2022-01-20","price":"1.2621"},
    {"date":"2022-01-21","price":"1.1202"},
    {"date":"2022-01-22","price":"1.0708"},
    {"date":"2022-01-23","price":"1.1241"},
    {"date":"2022-01-24","price":"1.0659"},
    {"date":"2022-01-25","price":"1.0393"}
  ]}
  
  return json.dumps([bitcoin, ethereum, tether, solana, cardano])

from IPython.display import HTML
HTML("<a href='https://{}.{}'>Crypto Pricing App</a>".format(os.environ['CDSW_ENGINE_ID'],os.environ['CDSW_DOMAIN']))

if __name__=="__main__":
  app.run(port=int(os.environ['CDSW_APP_PORT']))