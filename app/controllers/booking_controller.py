from flask import Blueprint, jsonify, request
from app.models.booking_model import Booking
from app.views.booking_view import BookingView
from app.config import Config
from app.utils import auth

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
        url = f"{Config.MICROSOFT_GRAPH_BASE_URL}/me/calendar/calendarView"
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
    """
    Busca uma reserva pelo ID
    """
    try:
        access_token = auth.get_access_token()
        headers = {'Authorization': 'Bearer ' + access_token}
        url = f"{Config.MICROSOFT_GRAPH_BASE_URL}/me/events/{id}"
        response = requests.get(url, headers=headers)
    if response.status_code == 200:
        booking = Booking.from_microsoft_graph(response.json())
        return BookingView.render(booking)
    else:
        return jsonify({'error': 'Reserva não encontrada'}), response.status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500
