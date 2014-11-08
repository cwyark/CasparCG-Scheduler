from flask import Flask, render_template
import os


port = 8000
host = '127.0.0.1'
debug = True
app = Flask(__name__)


@app.route('/')
def __index():
    return render_template('index.html', title='CasparCG Dashboard')


def run_server():
    app.run(port=port, host=host, debug=debug)


if __name__ == '__main__':
    run_server()
