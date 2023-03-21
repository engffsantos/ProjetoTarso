from flask import Blueprint, render_template, request, redirect, url_for
from app.models.evento_model import EventoModel

evento_view = Blueprint('evento_view', __name__)

@evento_view.route('/eventos')
def listar_eventos():
    eventos = EventoModel.listar_todos_eventos()
    return render_template('evento.html', eventos=eventos)

@evento_view.route('/eventos/novo', methods=['GET', 'POST'])
def novo_evento():
    if request.method == 'POST':
        EventoModel.criar_evento(request.form)
        return redirect(url_for('evento_view.listar_eventos'))
    else:
        return render_template('evento_form.html')

@evento_view.route('/eventos/editar/<int:id>', methods=['GET', 'POST'])
def editar_evento(id):
    evento = EventoModel.obter_evento_por_id(id)
    if request.method == 'POST':
        EventoModel.atualizar_evento(id, request.form)
        return redirect(url_for('evento_view.listar_eventos'))
    else:
        return render_template('evento_form.html', evento=evento)

@evento_view.route('/eventos/excluir/<int:id>')
def excluir_evento(id):
    EventoModel.excluir_evento(id)
    return redirect(url_for('evento_view.listar_eventos'))
