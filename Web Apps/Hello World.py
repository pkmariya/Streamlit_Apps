# My First Web App using Python Flask

from flask import Flask

app = Flask(__name__)

@app.route('/')

def hello():
    return "<h1>My First Web App using Python</h1>"

if __name__ == '__main__':
    app.run(debug=True)
