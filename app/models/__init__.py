from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from .booking_model import BookingModel
from .evento_model import EventoModel
from .local_model import LocalModel
from .pessoa_model import PessoaModel
