import os
from flask import Flask

app = Flask(__name__,static_url_path='')

@app.route('/')
def home():
  return "<script> window.location.href = '/flask/home.html'</script>"

if __name__=="__main__":
  app.run(host='127.0.0.1', port=int(os.environ['CDSW_APP_PORT']))