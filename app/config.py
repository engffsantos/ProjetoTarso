# Configurações da API do Booking da Microsoft
import secrets

CLIENT_ID = '13aec108-15d0-4a3c-b4f7-73d8edac29d1'
CLIENT_SECRET = '711ba862-9b43-410d-a6d8-f4441dd56fa9'
REDIRECT_URI = 'http://localhost:5000/getAToken'

# Configurações do Flask
SECRET_KEY = secrets.token_hex(16)
SESSION_TYPE = 'filesystem'
