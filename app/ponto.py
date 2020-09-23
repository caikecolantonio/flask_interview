from flask import Blueprint, current_app, request, jsonify
from .model import Batidas_Ponto
from .serializer import PontoSchema

bp_ponto = Blueprint('Batidas_Ponto', __name__)


@bp_ponto.route('/cadastrar_ponto', methods=['POST'])
def cadastrar():
   
    dados = request.get_json(force=True)
    usuario_id = dados['usuario_id']
    tipo_batida = dados['tipo_batida']
 
    ponto = Batidas_Ponto(usuario_id=usuario_id, tipo_batida=tipo_batida)

    current_app.db.session.add(ponto)
    current_app.db.session.commit()

    return PontoSchema().jsonify(ponto)

@bp_ponto.route('/mostrar_ponto', methods=['GET'])
def mostrar():
    result = Batidas_Ponto.query.all()
    return PontoSchema(many=True).jsonify(result), 200

    