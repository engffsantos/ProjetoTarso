from flask import Flask, render_template
from app.controllers import booking_controller, evento_controller, local_controller, pessoa_controller
from app.controllers.booking_controller import booking_controller
from app.views.evento_view import evento_view
from app.views.local_view import local_controller
from app.views.pessoa_view import pessoa_view


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/reservas')
def reservas():
    return booking_controller.get_all_bookings()

@app.route('/eventos')
def eventos():
    return evento_controller.get_all_events()

@app.route('/locais')
def locais():
    return local_controller.get_all_locals()

@app.route('/pessoas')
def pessoas():
    return pessoa_controller.get_all_people()

app.register_blueprint(booking_controller)
app.register_blueprint(evento_view)
app.register_blueprint(local_controller)
app.register_blueprint(pessoa_view)

if __name__ == '__main__':
    app.run()
