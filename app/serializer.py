from flask_marshmallow import Marshmallow 
from .model import Usuario
ma = Marshmallow()

def configure(app):
    ma.init_app(app)


class UsuarioSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario

