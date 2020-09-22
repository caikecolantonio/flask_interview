from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

def configure(app):
    db.init_app(app)
    app.db = db


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome_completo = db.Column(db.String(255))
    cpf = db.Column(db.String(14))
    email = db.Column(db.String(255))
    data_cadastro = db.Column(db.DateTime, default=datetime.now)