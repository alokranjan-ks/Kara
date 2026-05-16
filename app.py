import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Kara is awake. Connection to Google Cloud pending.</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
