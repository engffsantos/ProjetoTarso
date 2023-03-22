from flask import Blueprint, jsonify, request
from requests import auth

from app.models.booking_model import BookingModel
from app.views.booking_view import booking_view
from app.config import *
#from app.utils import auth

import requests

booking_bp = Blueprint('booking', __name__)

@booking_bp.route('/bookings', methods=['GET'])
@auth.login_required
def get_bookings():
    """
    Busca todas as reservas do usuário autenticado
    """
    try:
        access_token = auth.get_access_token()
        headers = {'Authorization': 'Bearer ' + access_token}
        url = f"{REDIRECT_URI}/me/calendar/calendarView"
        params = {
            'startDateTime': request.args.get('start'),
            'endDateTime': request.args.get('end')
        }
        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            bookings = Booking.from_microsoft_graph(response.json())
            return BookingView.render_many(bookings)
        else:
            return jsonify({'error': 'Erro ao buscar reservas'}), response.status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500
@booking_bp.route('/bookings/<id>', methods=['GET'])
@auth.login_required
def get_booking_by_id(id):
#    Busca uma reserva pelo ID
    try:
        access_token = auth.get_access_token()
        headers = {'Authorization': 'Bearer ' + access_token}
        url = f"{REDIRECT_URI}/me/events/{id}"
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            booking = Booking.from_microsoft_graph(response.json())
            return BookingView.render(booking)
        else:
            return jsonify({'error': 'Reserva não encontrada'}), response.status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500
booking_bp.route('/bookings', methods=['POST'])
@auth.login_required
def create_booking():
#Cria uma nova reserva
    try:
        data = request.get_json()
        new_booking = Booking.from_json(data)
        access_token = auth.get_access_token()
        headers = {'Authorization': 'Bearer ' + access_token}
        url = f"{REDIRECT_URI}/me/events"
        payload = new_booking.to_microsoft_graph()
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 201:
            booking_id = response.json().get('id')
            new_booking.id = booking_id
            return BookingView.render(new_booking), 201
        else:
            return jsonify({'error': 'Erro ao criar reserva'}), response.status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500
@booking_bp.route('/bookings/<id>', methods=['PUT'])
@auth.login_required
def update_booking(id):
    """
    Edita uma reserva existente
    """
    try:
        access_token = auth.get_access_token()
        headers = {'Authorization': 'Bearer ' + access_token}
        url = f"{REDIRECT_URI}/me/events/{id}"
        data = request.json
        response = requests.patch(url, headers=headers, json=data)

        if response.status_code == 200:
            updated_booking = Booking.from_microsoft_graph(response.json())
            return BookingView.render(updated_booking)
        else:
            return jsonify({'error': 'Erro ao atualizar reserva'}), response.status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500
@booking_bp.route('/bookings/int:id', methods=['DELETE'])
@auth.login_required
def cancel_booking(id):
    """
    Cancela uma reserva existente pelo ID
    """
    try:
        booking = Booking.get_by_id(id)
        if not booking:
            return jsonify({'error': 'Reserva não encontrada'}), 404
        access_token = auth.get_access_token()
        headers = {'Authorization': 'Bearer ' + access_token}
        url = f"{REDIRECT_URI}/me/events/{booking.event_id}/cancel"
        response = requests.post(url, headers=headers)
        if response.status_code == 202:
            Booking.delete(booking)
            return jsonify({'success': 'Reserva cancelada com sucesso'}), 200
        else:
            return jsonify({'error': 'Erro ao cancelar reserva'}), response.status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500
