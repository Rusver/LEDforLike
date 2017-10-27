from flask import Flask
from flask import json
from flask import Response
from flask import request
import os

app = Flask(__name__)

@app.route("/", methods =['GET', 'POST'])
def Welcome():
    return "Welcome to my page :)"

@app.route('/articles')
def api_articles():
    return 'List of articles'

@app.route('/articles/<articleid>')
def api_article(articleid):
    return 'You are reading ' + articleid

@app.route('/json', methods = ['GET', 'POST'])
def api_json():
    data = {k:v for k,v in request.args.items()}
    return json.dumps(data)

@app.route('/hello', methods = ['GET', 'POST'])
def api_hello():
    data = {
        'hello'  : 'world',
        'number' : 3
    }
    return json.dumps(data)

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = int(os.environ.get("PORT", 5000)))
