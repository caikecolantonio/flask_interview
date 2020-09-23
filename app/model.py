from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import enum

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

class Batidas_Ponto(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    data = db.Column(db.DateTime, default=datetime.now)
    tipo_badida = db.Column(db.Enum('entrada', 'saida'))
