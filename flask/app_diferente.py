#!/usr/bin/python3
import json
from pymongo import MongoClient
from bson.json_util import dumps
from datetime import datetime
from blueprint.site import site
from flask import Flask, jsonify, make_response, redirect, request, render_template

app = Flask(__name__)
app.register_blueprint(site)

#client = MongoClient('mongodb://user:senha@base')
client = MongoClient()
db = client.segunda
#for u in db.usuario.find():
#    print(u)
#exit()

@app.route('/')
def home():
#    return jsonify([json.loads(dumps(u)) for u in db.usuario.find()])
     return jsonify({"mensagem" : 'Rodando...'})

@app.route('/data')
def data():
    print('Paramahansa Yogananda')
    return jsonify({"Hoje" : datetime.now()})

@app.route('/naotembiscoito')
def naotemnadaaqui():
    return redirect('/')

@app.route('/cadastrar', methods=['POST'])
def post():
    dados = request.get_json()
    #Se dados for nulo, retornar 400
    #{'mensagem" : "corpo não pode ser vazio"}
    if dados is None:
        return make_response(jsonify({"mensagem" : "Corpo não pode ser vazio"}),400)
    dados['lapetina'] = 'fumacinha'
    return jsonify(dados)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
