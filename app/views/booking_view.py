from flask import Blueprint, render_template, request, redirect, url_for
from app.models.booking_model import BookingModel
from app.models.evento_model import EventoModel
from app.models.local_model import LocalModel
from app.models.pessoa_model import PessoaModel

booking_view = Blueprint('booking_view', __name__)

@booking_view.route('/reservas')
def listar_reservas():
    # Code to retrieve all bookings from the database
    reservas = BookingModel.listar_todas_reservas()
    # Render the booking.html template passing the reservas variable as context
    return render_template('booking.html', reservas=reservas)

@booking_view.route('/reservas/nova', methods=['GET', 'POST'])
def nova_reserva():
    eventos = EventoModel.listar_todos_eventos()
    locais = LocalModel.listar_todos_locais()
    pessoas = PessoaModel.listar_todas_pessoas()
    if request.method == 'POST':
        # Code to create a new booking in the database
        BookingModel.criar_reserva(request.form)
        return redirect(url_for('booking_view.listar_reservas'))
    else:
        return render_template('booking_form.html', eventos=eventos, locais=locais, pessoas=pessoas)

@booking_view.route('/reservas/editar/<int:id>', methods=['GET', 'POST'])
def editar_reserva(id):
    reserva = BookingModel.obter_reserva_por_id(id)
    eventos = EventoModel.listar_todos_eventos()
    locais = LocalModel.listar_todos_locais()
    pessoas = PessoaModel.listar_todas_pessoas()
    if request.method == 'POST':
        # Code to update the booking in the database
        BookingModel.atualizar_reserva(id, request.form)
        return redirect(url_for('booking_view.listar_reservas'))
    else:
        return render_template('booking_form.html', reserva=reserva, eventos=eventos, locais=locais, pessoas=pessoas)

@booking_view.route('/reservas/excluir/<int:id>')
def excluir_reserva(id):
    # Code to delete the booking from the database
    BookingModel.excluir_reserva(id)
    return redirect(url_for('booking_view.listar_reservas'))
