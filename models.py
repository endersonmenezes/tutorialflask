#  Desenvolvido em 2020, com <3 por Enderson Menezes.

from manage import db


class Teste(db.Model):
    __tablename__ = 'teste_db'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return 'Email:{} <{}>'.format(self.email, self.id)

