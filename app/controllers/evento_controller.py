from datetime import datetime

from app.auth import auth
from flask import jsonify, request

from app import db
from app.controllers import evento_controller as controller
from app.views import evento_view


@evento_controller.route('/eventos', methods=['GET'])
@auth.login_required
def get_events():
    """
    Busca todos os eventos do usuário autenticado
    """
    try:
        events = controller.get_all_events()
        return evento_view.render_many(events)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@evento_controller.route('/events/<id>', methods=['GET'])
@auth.login_required
def get_event_by_id(id):
    """
    Busca um evento pelo ID
    """
    try:
        event = controller.get_event_by_id(id)
        return evento_view.render(event)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@evento_controller.route('/eventos', methods=['POST'])
@auth.login_required
def create_event():
    """
    Cria um novo evento
    """
    try:
        data = request.json
        event = controller.create_event(data)
        return evento_view.render(event), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
@evento_controller.route('/eventos/<id>', methods=['PUT'])
@auth.login_required
def update_event(id):
    """
    Edita um evento existente pelo ID
    """
    try:
        data = request.get_json()
        event = Evento.query.filter_by(id=id).first()
        if not event:
            return jsonify({'error': 'Evento não encontrado'}), 404

        event.title = data['title']
        event.start_time = datetime.fromisoformat(data['start_time'])
        event.end_time = datetime.fromisoformat(data['end_time'])
        event.location_id = data['location_id']
        db.session.commit()

        return evento_view.render(event), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@evento_controller.route('/eventos/<id>', methods=['DELETE'])
@auth.login_required
def delete_event(id):
    """
    Exclui um evento existente pelo ID
    """
    try:
        event = evento_view.query.filter_by(id=id).first()
        if not event:
            return jsonify({'error': 'Evento não encontrado'}), 404

        db.session.delete(event)
        db.session.commit()

        return '', 204
    except Exception as e:
        return jsonify({'error': str(e)}), 500
