from app import db

class LocalModel(db.Model):
    __tablename__ = 'local'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    endereco = db.Column(db.String(120), nullable=False)

    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    def json(self):
        return {'id': self.id, 'nome': self.nome, 'endereco': self.endereco}

    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, nome=None, endereco=None):
        if nome:
            self.nome = nome
        if endereco:
            self.endereco = endereco
        self.save()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
