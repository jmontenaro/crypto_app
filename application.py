#select
#  from_timestamp(to_timestamp(a.ts), 'yyyy-MM-dd') `date`
#  , a.digital_currency_code code
#  , a.close
#from
#  crypto_timeseries a
#inner join (
#  select
#    max(ts) ts,
#    digital_currency_code
#  from
#    crypto_timeseries
#  group by
#    digital_currency_code,
#    date_trunc('DAY', to_timestamp(ts))
#) b on
#  a.ts = b.ts
#  and a.digital_currency_code = b.digital_currency_code
#order by
#  code,
#  `date`;

import json
import logging
import os
from flask import Flask, render_template
from pyspark.sql.types import *
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

  df = spark.sql("select * from crypto_db.crypto_monthly_ext order by code, date").collect()
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