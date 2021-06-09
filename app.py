from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello There"

@app.route('/dk')
def dk():
    return "Hello Digvijay"

if __name__ == '__main__':
    app.run(debug=True)
