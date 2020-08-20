import os
import shutil
import requests
import tempfile

from gevent.pywsgi import WSGIServer
from flask import Flask, after_this_request, render_template, request, send_file

UPLOAD_FOLDER = '/tmp'
ALLOWED_EXTENSIONS = set(['doc', 'docx', 'xls', 'xlsx'])

app = Flask(__name__)


@app.route('/', methods=['GET'])
def api():
    if request.method == 'GET':
        return "Hello World"
 
#return send_file(output_file_path, mimetype='application/pdf')


if __name__ == "__main__":
    http_server = WSGIServer(('', int(os.environ.get('PORT', 8080))), app)
    http_server.serve_forever()
