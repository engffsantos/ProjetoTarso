from flask import Blueprint, render_template, request, redirect, url_for
from app.models.pessoa_model import PessoaModel

pessoa_controller = Blueprint('pessoa_controller', __name__)

@pessoa_controller.route('/pessoas')
def listar_pessoas():
    # Code to retrieve all people from the database
    pessoas = PessoaModel.listar_todas_pessoas()
    # Render the pessoa.html template passing the pessoas variable as context
    return render_template('pessoa.html', pessoas=pessoas)

@pessoa_controller.route('/pessoas/nova', methods=['GET', 'POST'])
def nova_pessoa():
    if request.method == 'POST':
        # Code to create a new person in the database
        PessoaModel.criar_pessoa(request.form)
        return redirect(url_for('pessoa_controller.listar_pessoas'))
    else:
        return render_template('pessoa_form.html')

@pessoa_controller.route('/pessoas/editar/<int:id>', methods=['GET', 'POST'])
def editar_pessoa(id):
    pessoa = PessoaModel.obter_pessoa_por_id(id)
    if request.method == 'POST':
        # Code to update the person in the database
        PessoaModel.atualizar_pessoa(id, request.form)
        return redirect(url_for('pessoa_controller.listar_pessoas'))
    else:
        return render_template('pessoa_form.html', pessoa=pessoa)

@pessoa_controller.route('/pessoas/excluir/<int:id>')
def excluir_pessoa(id):
    # Code to delete the person from the database
    PessoaModel.excluir_pessoa(id)
    return redirect(url_for('pessoa_controller.listar_pessoas'))
