import os
import requests


from gevent.pywsgi import WSGIServer
from flask import Flask, after_this_request, render_template, request, send_file


app = Flask(__name__)


@app.route('/', methods=['GET'])
def api():
    return "Hello World"

if __name__ == "__main__":
    http_server = WSGIServer(('', int(os.environ.get('PORT', 8080))), app)
    http_server.serve_forever()
