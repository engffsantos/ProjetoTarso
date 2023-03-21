from flask import Blueprint, jsonify, request
from app.models.pessoa_model import Pessoa
from app.views.pessoa_view import PessoaView
from app.config import Config
from app.auth import auth
import requests


pessoa_bp = Blueprint('pessoa', __name__)


@pessoa_bp.route('/pessoas', methods=['GET'])
@auth.login_required
def get_pessoas():
    """
    Busca todas as pessoas do usuário autenticado
    """
    try:
        access_token = auth.get_access_token()
        headers = {'Authorization': 'Bearer ' + access_token}
        url = f"{Config.MICROSOFT_GRAPH_BASE_URL}/me/people"
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            pessoas = Pessoa.from_microsoft_graph(response.json())
            return PessoaView.render_many(pessoas)
        else:
            return jsonify({'error': 'Erro ao buscar pessoas'}), response.status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@pessoa_bp.route('/pessoas/<id>', methods=['GET'])
@auth.login_required
def get_pessoa_by_id(id):
    """
    Busca uma pessoa pelo ID
    """
    try:
        access_token = auth.get_access_token()
        headers = {'Authorization': 'Bearer ' + access_token}
        url = f"{Config.MICROSOFT_GRAPH_BASE_URL}/users/{id}"
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            pessoa = Pessoa.from_microsoft_graph(response.json())
            return PessoaView.render_one(pessoa)
        else:
            return jsonify({'error': 'Erro ao buscar pessoa'}), response.status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@pessoa_bp.route('/pessoas', methods=['POST'])
@auth.login_required
def create_pessoa():
    """
    Cria uma nova pessoa
    """
    try:
        data = request.json
        pessoa = Pessoa.create(**data)
        return PessoaView.render_one(pessoa), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@pessoa_bp.route('/pessoas/<id>', methods=['PUT'])
@auth.login_required
def update_pessoa(id):
    """
    Edita uma pessoa existente pelo ID
    """
    try:
        data = request.json
        pessoa = Pessoa.get_by_id(id)
        pessoa.update(**data)
        return PessoaView.render_one(pessoa)
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@pessoa_bp.route('/pessoas/<id>', methods=['DELETE'])
@auth.login_required
def delete_pessoa(id):
    """
    Exclui uma pessoa pelo ID
    """
    try:
        pessoa = Pessoa.get_by_id(id)
        pessoa.delete()
        return '', 204
    except Exception as e:
        return jsonify({'error': str(e)}), 400



# from flask import Blueprint, render_template, request, redirect, url_for
# from app.models.pessoa_model import PessoaModel
#
# pessoa_controller = Blueprint('pessoa_controller', __name__)
#
# @pessoa_controller.route('/pessoas')
# def listar_pessoas():
#     # Code to retrieve all people from the database
#     pessoas = PessoaModel.listar_todas_pessoas()
#     # Render the pessoa.html template passing the pessoas variable as context
#     return render_template('pessoa.html', pessoas=pessoas)
#
# @pessoa_controller.route('/pessoas/nova', methods=['GET', 'POST'])
# def nova_pessoa():
#     if request.method == 'POST':
#         # Code to create a new person in the database
#         PessoaModel.criar_pessoa(request.form)
#         return redirect(url_for('pessoa_controller.listar_pessoas'))
#     else:
#         return render_template('pessoa_form.html')
#
# @pessoa_controller.route('/pessoas/editar/<int:id>', methods=['GET', 'POST'])
# def editar_pessoa(id):
#     pessoa = PessoaModel.obter_pessoa_por_id(id)
#     if request.method == 'POST':
#         # Code to update the person in the database
#         PessoaModel.atualizar_pessoa(id, request.form)
#         return redirect(url_for('pessoa_controller.listar_pessoas'))
#     else:
#         return render_template('pessoa_form.html', pessoa=pessoa)
#
# @pessoa_controller.route('/pessoas/excluir/<int:id>')
# def excluir_pessoa(id):
#     # Code to delete the person from the database
#     PessoaModel.excluir_pessoa(id)
#     return redirect(url_for('pessoa_controller.listar_pessoas'))
