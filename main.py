import os

from flask import Flask, jsonify, render_template


app = Flask(__name__)


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
