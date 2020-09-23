from flask_marshmallow import Marshmallow 
from .model import Usuario
from .model import Batidas_Ponto

ma = Marshmallow()

def configure(app):
    ma.init_app(app)


class UsuarioSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario

class PontoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Batidas_Ponto
