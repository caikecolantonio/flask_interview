from flask import Blueprint, current_app, request, jsonify
from .model import Usuario
from .serializer import UsuarioSchema

bp_usuarios = Blueprint('usuarios', __name__)

@bp_usuarios.route('/mostrar', methods=['GET'])
def mostrar():
    result = Usuario.query.all()
    return UsuarioSchema(many=True).jsonify(result), 200

@bp_usuarios.route('/deletar/<identificador>', methods=['DELETE'])
def deletar(identificador):
    Usuario.query.filter(Usuario.id == identificador).delete()
    current_app.db.session.commit()
    return jsonify('Deletado!!')

@bp_usuarios.route('/modificar/<identificador>', methods=['PATCH'])
def modificar(identificador):
    bs = UsuarioSchema()
    nome_completo = request.json.get('nome_completo', '')
    cpf = request.json.get('cpf', '')
    email = request.json.get('email', '')

    alterar = Usuario.query.get(identificador)

    alterar.nome_completo = nome_completo
    alterar.cpf = cpf
    alterar.email = email

    current_app.db.session.add(alterar)
    current_app.db.session.commit()

    return UsuarioSchema().jsonify(alterar), 200 


@bp_usuarios.route('/cadastrar', methods=['POST'])
def cadastrar():
    bs = UsuarioSchema()
    usuario = bs.load(request.json)
    nome_completo = request.json.get('nome_completo', '')
    cpf = request.json.get('cpf', '')
    email = request.json.get('email', '')

    usuario = Usuario(nome_completo=nome_completo, cpf=cpf, email=email)

    current_app.db.session.add(usuario)
    current_app.db.session.commit()

    return bs.jsonify(usuario)


