from app import db
from datetime import datetime

class BookingModel(db.Model):
    __tablename__ = 'booking'

    id = db.Column(db.Integer, primary_key=True)
    pessoa_id = db.Column(db.Integer, db.ForeignKey('pessoa.id'), nullable=False)
    evento_id = db.Column(db.Integer, db.ForeignKey('evento.id'), nullable=False)
    data_reserva = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, pessoa_id, evento_id):
        self.pessoa_id = pessoa_id
        self.evento_id = evento_id

    @staticmethod
    def get_all():
        return BookingModel.query.all()

    @staticmethod
    def get_by_id(id):
        return BookingModel.query.filter_by(id=id).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
