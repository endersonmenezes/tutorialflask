import os

from flask import Flask, jsonify, render_template

import requests


app = Flask(__name__)


@app.route("/dolar")
def api_dolar():
    """
    Rota que devolve a cotação do dolar!
    :return: jsonify
    """
    api_finance = 'https://api.hgbrasil.com/finance'
    r_api = requests.get(api_finance)
    r_api_data = r_api.json()
    dolar_value = r_api_data['results']['currencies']['USD']['buy']
    return jsonify({'dolar': dolar_value})

@app.route("/json")
def json_example():
    """
    Rota da Página Inicial!
    :return: Jsonify
    """
    return jsonify({'detail': 'Seja bem vindo a Orbital!'})


@app.route("/")
def home():
    """
    Rota de Exemplo JSON
    :return: Pure HTML
    """
    return "<a href='/json'> Clique aqui para ver um exemplo em Json </a> <br>" \
           "<a href='/html'> Clique aqui para ver um exemplo em HTML </a>"


@app.route("/html")
def html_example():
    """
    Rota de Exemplo HTML
    :return: Jsonify
    """
    return render_template("index.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
