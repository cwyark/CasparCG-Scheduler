from flask import Flask, render_template, request


port = 8000
host = '127.0.0.1'
debug = True
app = Flask(__name__)


@app.route('/')
def __index():
    return render_template('index.html', title='CasparCG Dashboard')


@app.route('/ontheair/<name>/<timestamp>/<tag>', methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def __OTA_handler(name, timestamp, tag):
    if request.method in ['GET', 'POST', 'PATCH']:
        return "method %sis not allowed" % request.method
    elif request.method == 'PUT':
        return "PUT the data"
    elif request.method == 'DELETE':
        return "DELETE  the data"


def run_server():
    app.run(port=port, host=host, debug=debug)


if __name__ == '__main__':
    run_server()
