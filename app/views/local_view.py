from flask import Blueprint, render_template, request, redirect, url_for
from app.models.local_model import LocalModel

local_controller = Blueprint('local_controller', __name__)

@local_controller.route('/locais')
def listar_locais():
    locais = LocalModel.listar_todos_locais()
    return render_template('local.html', locais=locais)

@local_controller.route('/locais/novo', methods=['GET', 'POST'])
def novo_local():
    if request.method == 'POST':
        LocalModel.criar_local(request.form)
        return redirect(url_for('local_controller.listar_locais'))
    else:
        return render_template('local_form.html')

@local_controller.route('/locais/editar/<int:id>', methods=['GET', 'POST'])
def editar_local(id):
    local = LocalModel.obter_local_por_id(id)
    if request.method == 'POST':
        LocalModel.atualizar_local(id, request.form)
        return redirect(url_for('local_controller.listar_locais'))
    else:
        return render_template('local_form.html', local=local)

@local_controller.route('/locais/excluir/<int:id>')
def excluir_local(id):
    LocalModel.excluir_local(id)
    return redirect(url_for('local_controller.listar_locais'))
