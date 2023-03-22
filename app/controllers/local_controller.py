from flask import Blueprint, jsonify, request
from app.models.local_model import *
from app.views.local_view import *
from app.auth import auth

local_bp = Blueprint('local_bp', __name__)

# GET /locals - busca todos os locais
@local_bp.route('/locals', methods=['GET'])
@auth.login_required
def get_locals():
    """
    Busca todos os locais cadastrados
    """
    try:
        locals = Local.get_all()
        return LocalView.render_many(locals)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# GET /locals/<id> - busca local pelo ID
@local_bp.route('/locals/<id>', methods=['GET'])
@auth.login_required
def get_local_by_id(id):
    """
    Busca um local pelo ID
    """
    try:
        local = Local.get_by_id(id)
        if local:
            return LocalView.render(local)
        else:
            return jsonify({'error': 'Local não encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# POST /locals - cria um novo local
@local_bp.route('/locals', methods=['POST'])
@auth.login_required
def create_local():
    """
    Cria um novo local
    """
    try:
        data = request.json
        local = Local.create(data)
        return LocalView.render(local), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# PUT /locals/<id> - edita um local existente
@local_bp.route('/locals/<id>', methods=['PUT'])
@auth.login_required
def update_local(id):
    """
    Edita um local existente
    """
    try:
        data = request.json
        local = Local.update(id, data)
        if local:
            return LocalView.render(local)
        else:
            return jsonify({'error': 'Local não encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# DELETE /locals/<id> - exclui um local existente
@local_bp.route('/locals/<id>', methods=['DELETE'])
@auth.login_required
def delete_local(id):
    """
    Exclui um local existente
    """
    try:
        local = Local.delete(id)
        if local:
            return '', 204
        else:
            return jsonify({'error': 'Local não encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
