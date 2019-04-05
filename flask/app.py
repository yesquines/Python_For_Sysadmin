import os, sys
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"status" : "Rodando...", "version" : sys.version})

APP_HOST = os.environ['APP_HOST']
APP_PORT = int(os.environ['APP_PORT'])
APP_DEBUG = True if 'APP_DEBUG' in os.environ else False

app.run(host=APP_HOST, port=APP_PORT, debug=APP_DEBUG)
