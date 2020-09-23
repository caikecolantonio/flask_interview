from flask import Blueprint, current_app, request, jsonify, render_template
from .model import Usuario
from .serializer import UsuarioSchema

bp_usuarios = Blueprint('usuarios', __name__)

@bp_usuarios.route('/mostrar', methods=['GET'])
def mostrar():
    result = Usuario.query.all()
    return UsuarioSchema(many=True).jsonify(result), 200

@bp_usuarios.route('/deletar/<identificador>', methods=['GET'])
def deletar(identificador):
    Usuario.query.filter(Usuario.id == identificador).delete()
    current_app.db.session.commit()
    return jsonify('Deletado!!')

@bp_usuarios.route('/modificar/<identificador>', methods=['POST'])
def modificar(identificador):
    bs = UsuarioSchema()
    query = Usuario.query.filter(Usuario.id == identificador)
    query.update(request.json)
    current_app.db.session.commit()
    return bs.jsonify(query.first())

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


