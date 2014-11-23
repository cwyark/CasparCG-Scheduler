from flask import Flask, render_template, request
import models

port = 8000
host = '127.0.0.1'
debug = True
app = Flask(__name__)


@app.route('/')
def __index():
    return render_template('index.html', title='CasparCG Dashboard')


@app.route('/testclient')
def __testclient():
    return render_template('testclient.html', title='CasparCG Dashboard')


@app.route('/insert/<name>/<timestamp>', methods=['GET', 'POST', 'DELETE'])
def __OTA_handler(name, timestamp):
    if request.method == 'GET':
        return "Get the data"
    elif request.method == 'POST':
        return "PUT the da"
    elif request.method == 'DELETE':
        return "DELETE  the data"


def run_server():
    app.run(port=port, host=host, debug=debug)


if __name__ == '__main__':
    run_server()
