from flask import Flask, render_template

from app.controllers import booking_controller, evento_controller, local_controller, pessoa_controller
from app.controllers.booking_controller import booking_controller
from app.views.evento_view import evento_view
from app.views.local_view import local_controller
from app.views.pessoa_view import pessoa_view
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

# @app.route('/login')
# def login():
#     # Cria um estado único para evitar ataques de CSRF
#     state = str(uuid.uuid4())
#     session['state'] = state
#
#     # Cria uma instância do aplicativo de cliente confidencial do MSAL
#     cca = ConfidentialClientApplication(
#         app.config['CLIENT_ID'],
#         client_credential=app.config['CLIENT_SECRET']
#     )
#
#     # Cria a URL de autorização
#     auth_url = cca.get_authorization_request_url(
#         scopes=['https://graph.microsoft.com/.default'],
#         state=state,
#         redirect_uri=app.config['REDIRECT_URI']
#     )
#
#     return redirect(auth_url)
#
# @app.route('/callback')
# def callback():
#     # Verifica o estado para evitar ataques de CSRF
#     if request.args.get('state') != session.get('state'):
#         return redirect('/login')
#
#     # Cria uma instância do aplicativo de cliente confidencial do MSAL
#     cca = ConfidentialClientApplication(
#         app.config['CLIENT_ID'],
#         client_credential=app.config['CLIENT_SECRET']
#     )
#
#     # Obtém um token de acesso usando o código de autorização
#     result = cca.acquire_token_by_authorization_code(
#         request.args['code'],
#         scopes=['https://graph.microsoft.com/.default'],
#         redirect_uri=app.config['REDIRECT_URI']
#     )
#
#     # Obtém informações do usuário usando o token de acesso
#     response = requests.get(
#         'https://graph.microsoft.com/v1.0/me',
#         headers={'Authorization': 'Bearer ' + result['access_token']}
#     )
#     session['user'] = response.json()
#
#     return redirect('/')

if __name__ == '__main__':
    app.run()
