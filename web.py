from flask import Flask, render_template, request
import settings


app = Flask(__name__)


@app.route('/')
def __index():
    return render_template('index.html', title='CasparCG Dashboard')


@app.route('/testclient')
def __testclient():
    return render_template('testclient.html', title='CasparCG Dashboard')


@app.route('/ontheair/<name>/<timestamp>/<tag>', methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def __OTA_handler(name, timestamp, tag):
    if request.method in ['POST', 'PATCH']:
        return "method %s is not allowed" % request.method
    elif request.method == 'GET':
        return "Get the data"
    elif request.method == 'PUT':
        return "PUT the data"
    elif request.method == 'DELETE':
        return "DELETE  the data"


def run_server():
    app.run(port=settings.__WEBCLIENT_PORT__, host=settings.__WEBCLIENT_IP__, debug=settings.__WEBCLIENT_DEBUG__)


if __name__ == '__main__':
    run_server()
