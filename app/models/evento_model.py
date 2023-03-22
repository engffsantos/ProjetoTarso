from app import db

class EventoModel(db.Model):
    __tablename__ = 'evento'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    descricao = db.Column(db.String(255), nullable=True)
    data_inicio = db.Column(db.DateTime(), nullable=False)
    data_fim = db.Column(db.DateTime(), nullable=False)
    local_id = db.Column(db.Integer, db.ForeignKey('local.id'), nullable=False)

    def __init__(self, nome, descricao, data_inicio, data_fim, local_id):
        self.nome = nome
        self.descricao = descricao
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.local_id = local_id
