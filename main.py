import os

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    """
    Rota da Página Inicial!
    :return: Jsonify
    """
    return jsonify({'detail': 'Seja bem vindo a Orbital!'})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
