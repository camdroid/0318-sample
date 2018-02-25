from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html', name='Cam')

@app.route('/world')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
