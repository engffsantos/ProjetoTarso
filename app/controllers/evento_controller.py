from app.controllers import evento_controller as controller
from flask import jsonify, request
from app.auth import auth
@evento_bp.route('/events', methods=['GET'])
@auth.login_required
def get_events():
    """
    Busca todos os eventos do usuário autenticado
    """
    try:
        events = controller.get_all_events()
        return EventoView.render_many(events)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@evento_bp.route('/events/<id>', methods=['GET'])
@auth.login_required
def get_event_by_id(id):
    """
    Busca um evento pelo ID
    """
    try:
        event = controller.get_event_by_id(id)
        return EventoView.render(event)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@evento_bp.route('/events', methods=['POST'])
@auth.login_required
def create_event():
    """
    Cria um novo evento
    """
    try:
        data = request.json
        event = controller.create_event(data)
        return EventoView.render(event), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
@evento_bp.route('/events/<id>', methods=['PUT'])
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

        return EventoView.render(event), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@evento_bp.route('/events/<id>', methods=['DELETE'])
@auth.login_required
def delete_event(id):
    """
    Exclui um evento existente pelo ID
    """
    try:
        event = Evento.query.filter_by(id=id).first()
        if not event:
            return jsonify({'error': 'Evento não encontrado'}), 404

        db.session.delete(event)
        db.session.commit()

        return '', 204
    except Exception as e:
        return jsonify({'error': str(e)}), 500
