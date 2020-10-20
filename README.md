# Tutorial Flask on Heroku

## Exemplos Abordados

- Capturando Dados com Requests/BeautifulSoup
```
http://localhost:5000/wikipedia
```
    
- Exemplo retorno em HTML
``` 
http://localhost:5000/html
```
- Exemplo de retorno em JSON
``` 
http://localhost:5000/json
```
- Exemplo de Consumo de API (Dolar)
``` 
http://localhost:5000/dolar
```
- Exemplo utilizando Banco de Dados
``` 
http://localhost:5000/bd
```

## Como Começar

Para testar e visualizar o projeto localmente será necessário que você tenha o Git instalado, e clone o projeto.
```
git clone https://github.com/endersonmenezes/tutorialflask.git
```
Esse projeto foi construido em Python, é necessário que você tenha o Python instalado e execute os comandos abaixo, dependendo da sua instalação substituia python por python3.
```shell
# Crie uma venv para trabalhar com esse projeto.
python -m venv flaskteste

# Ative sua virtualenv para entrar em uma ambiente de teste para o projeto.
source flaskteste/bin/activate

# Instale todos os requisitos listados no arquivo requirements, pode ser necessário atualizar o pip, caso receba alguma mensagem pedindo.
pip install -r requirements.txt
```
O nosso projeto já possui algumas migrações de banco de dados como exemplo, você precisar executar elas e automaticamente será criado um banco de dados app.db em SQLite3.
```shell
(flaskteste) python manage.py db upgrade
```

Você já se encontra preparado para rodar esse servidor!
```shell
(flaskteste) python manage.py runserver
```

## Outras informações

- Comandos para administrar o banco de dados;
- Adicionar o postgres no Heroku - [Link](https://elements.heroku.com/addons/heroku-postgresql)

## Contribuidores

- [Ana Paula Maganha](https://github.com/anamaganha)