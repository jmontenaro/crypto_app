import os
from flask import Flask, render_template

app = Flask(__name__,static_url_path='')

@app.route('/')
def home():
  return render_template("home.html")

if __name__=="__main__":
  app.run(host='127.0.0.1', port=int(os.environ['CDSW_APP_PORT']))