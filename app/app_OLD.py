from flask import Flask, redirect, request, session
from msal import ConfidentialClientApplication
import uuid
import requests

app = Flask(__name__)
app.config.from_pyfile('config.py')

@app.route('/')
def index():
    if not session.get('user'):
        return redirect('/login')
    return 'Olá, {}!'.format(session['user']['displayName'])

@app.route('/login')
def login():
    # Cria um estado único para evitar ataques de CSRF
    state = str(uuid.uuid4())
    session['state'] = state

    # Cria uma instância do aplicativo de cliente confidencial do MSAL
    cca = ConfidentialClientApplication(
        app.config['CLIENT_ID'],
        client_credential=app.config['CLIENT_SECRET']
    )

    # Cria a URL de autorização
    auth_url = cca.get_authorization_request_url(
        scopes=['https://graph.microsoft.com/.default'],
        state=state,
        redirect_uri=app.config['REDIRECT_URI']
    )

    return redirect(auth_url)

@app.route('/callback')
def callback():
    # Verifica o estado para evitar ataques de CSRF
    if request.args.get('state') != session.get('state'):
        return redirect('/login')

    # Cria uma instância do aplicativo de cliente confidencial do MSAL
    cca = ConfidentialClientApplication(
        app.config['CLIENT_ID'],
        client_credential=app.config['CLIENT_SECRET']
    )

    # Obtém um token de acesso usando o código de autorização
    result = cca.acquire_token_by_authorization_code(
        request.args['code'],
        scopes=['https://graph.microsoft.com/.default'],
        redirect_uri=app.config['REDIRECT_URI']
    )

    # Obtém informações do usuário usando o token de acesso
    response = requests.get(
        'https://graph.microsoft.com/v1.0/me',
        headers={'Authorization': 'Bearer ' + result['access_token']}
    )
    session['user'] = response.json()

    return redirect('/')

if __name__ == '__main__':
    app.run()
