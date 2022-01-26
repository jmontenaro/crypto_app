import json
import logging
import os
from flask import Flask, render_template
from pyspark.sql import SparkSession

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)

@app.route('/')
def home():
  return render_template("home.html")

@app.route('/sample_data')
def sample_data():
  spark = SparkSession \
    .builder \
    .appName("SparkSQL") \
    .master("local[*]") \
    .getOrCreate()

  dataset = []
  df = spark.read.option("header", True).csv("static/prices.csv").collect()
  for row in df:
    for i in dataset:
      if (i.get("name") == row['code']):
        i.get("pricing_history").append({"date":row['date'], "price":row['close']})
        break
    else:
      dataset.append({"name":row['code'], "pricing_history":[{"date":row['date'], "price":row['close']}]})

  return json.dumps(dataset)

from IPython.display import HTML
HTML("<a href='https://{}.{}'>Crypto Pricing App</a>".format(os.environ['CDSW_ENGINE_ID'],os.environ['CDSW_DOMAIN']))

if __name__=="__main__":
  app.run(port=int(os.environ['CDSW_APP_PORT']))