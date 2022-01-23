import os
from flask import Flask, render_template

#app = Flask(__name__,static_url_path='')
app = Flask(__name__)

@app.route('/')
def home():
  return render_template("home.html")

from IPython.display import HTML
HTML("<a href='https://{}.{}'>Click ME!</a>".format(os.environ['CDSW_ENGINE_ID'],os.environ['CDSW_DOMAIN']))

if __name__=="__main__":
  app.run(port=int(os.environ['CDSW_APP_PORT']))