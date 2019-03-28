#!/usr/bin/python3
from datetime import datetime
from flask import Blueprint, render_template

site = Blueprint('site', __name__, url_prefix='/site')

@site.route('/')
def site_home():
    dados = [{'id' : '02', 'nome' : 'Paramahansa Yogananda'}]
    dados.append({'id' : '03', 'nome' : 'Gabriel Pensador'})
    dados.append({'id' : '04', 'nome' : 'João Batista'})
    return render_template('index.html', items=["1","2","3","4","PHP - Potato High Potato"], usuarios=dados)

@site.route('/contato')
def contato():
    return render_template('contato.html')
