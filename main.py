import os

from flask import Flask, jsonify, render_template, request as flask_request

from bs4 import BeautifulSoup

from flask_sqlalchemy import SQLAlchemy

import requests

app = Flask(__name__)
app.config.from_object(os.environ.get('APP_SETTINGS', 'config.DevelopmentConfig'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Teste


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


@app.route("/wikipedia")
def api_wikipedia():
    """
    Rota que devolve dados de uma página no wikipedia.
    :return:  jsonify
    """
    search = flask_request.args.get('search', None)
    url = flask_request.url
    if search:
        api_wikipedia = 'https://pt.wikipedia.org/wiki/{}'.format(search)
        r_api = requests.get(api_wikipedia)
        if r_api.status_code != 200:
            return jsonify({'detail': 'Não conseguimos encontrar nada com o parametro indicado.'})
        r_api_bs = BeautifulSoup(r_api.text, 'html.parser')
        title = r_api_bs.find(id='firstHeading')
        body = r_api_bs.find(id='bodyContent')
        div_class_table = r_api_bs.find_all('div', attrs={'class': 'mw-parser-output'})
        div_class_table = div_class_table[0]
        p_from_table = div_class_table.find('p')
        return jsonify({
            'titulo': title.text,
            'corpo': p_from_table.text,
        })
    else:
        return jsonify({
            'detail': 'Erro, você precisa informar um parametro de busca!',
            'example': '{}?search=<SUA_BUSCA_AQUI>'.format(url)
        })


@app.route("/json")
def json_example():
    """
    Rota da Página Inicial!
    :return: Jsonify
    """
    return jsonify({'detail': 'Seja bem vindo a Orbital!'})


@app.route("/html")
def html_example():
    """
    Rota de Exemplo HTML
    :return: Jsonify
    """
    return render_template("index.html")


@app.route("/bd")
def bd():
    """
    Rota de Exemplo HTML
    :return: Jsonify
    """
    method = flask_request.args.get('method')
    if method == 'add':
        email = flask_request.args.get('email', None)

        # SE O BANCO TIVER LOTADO
        query = Teste.query.all()
        query_len = len(query)
        if query_len > 10:
            for email in query:
                db.session.delete(email)
            db.session.commit()
        # SE O BANCO TIVER LOTADO

        if email:
            email_exists = Teste.query.filter_by(email=email).first()
            if email_exists:
                return jsonify({'detail': 'Este e-mail já existe no banco de dados.'})
            else:
                add_email = Teste(email=email)
                db.session.add(add_email)
                db.session.commit()
                return jsonify({
                    'detail': 'Success',
                    'email_added': email,
                })
        else:
            return jsonify({'detail': 'Você precisa enviar um e-mail no parametro email'})
    elif method == 'get':
        emails = Teste.query.all()
        data_return = []
        for email in emails:
            data_return.append(email.email)
        return jsonify({
            'detail': 'method get',
            'emails': data_return,
        })
    else:
        return jsonify({
            'detail': 'Você precisa enviar um metódo válido para está requisição.',
            'available': 'add|get',
        })


@app.route("/")
def home():
    """
    Rota de Exemplo JSON
    :return: Pure HTML
    """
    return "<a href='/json'> Clique aqui para ver um exemplo em Json </a> <br>" \
           "<a href='/html'> Clique aqui para ver um exemplo em HTML </a> <br>" \
           "<a href='/dolar'> Clique aqui para ver a cotação do Dolar </a> <br>" \
           "<a href='/wikipedia'> Clique aqui para ver um exemplo consumindo dados do Wikipedia! </a> <br>" \
           "<a href='/bd'> Clique aqui para ver um exemplo em Banco de Dados </a> <br>"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
