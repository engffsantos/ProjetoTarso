from app import db


class PessoaModel(db.Model):
    __tablename__ = 'pessoas'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    telefone = db.Column(db.String(20))
    cpf = db.Column(db.String(14), nullable=False, unique=True)

    def __init__(self, nome, email, telefone, cpf):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.cpf = cpf

    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "telefone": self.telefone,
            "cpf": self.cpf
        }

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_cpf(cls, cpf):
        return cls.query.filter_by(cpf=cpf).first()

    @classmethod
    def list_all(cls):
        return cls.query.all()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, nome, email, telefone, cpf):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.cpf = cpf
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
