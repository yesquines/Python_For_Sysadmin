#!/usr/bin/python3
from datetime import datetime
from flask import Flask, jsonify, make_response, redirect, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
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

@app.route('/site')
def site():
    dados = [{'id' : '02', 'nome' : 'Paramahansa Yogananda'}]
    dados.append({'id' : '03', 'nome' : 'Gabriel Pensador'})
    dados.append({'id' : '04', 'nome' : 'João Batista'})
    return render_template('index.html', nome="Yago", items=["1","2","3","4","PHP - Potato High Potato"], usuarios=dados)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
