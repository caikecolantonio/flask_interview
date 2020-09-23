from flask import Blueprint, current_app, request, jsonify
from .model import Batidas_Ponto
from .serializer import PontoSchema

bp_ponto = Blueprint('batidas_ponto', __name__)

@bp_ponto.route('/cadastrar_ponto', methods=['POST'])
def cadastrar():
    bs = PontoSchema()
    ponto = bs.load(request.json)
    usuario_id = request.json.get('usuario_id', '')
    tipo_badida = request.json.get('tipo_badida', '')
 
    ponto = Batidas_Ponto(usuario_id=usuario_id, tipo_badida=tipo_badida)

    current_app.db.session.add(ponto)
    current_app.db.session.commit()

    return bs.jsonify(ponto)

@bp_ponto.route('/mostrar', methods=['GET'])
def mostrar():
    result = Batidas_Ponto.query.all()
    return PontoSchema(many=True).jsonify(result), 200