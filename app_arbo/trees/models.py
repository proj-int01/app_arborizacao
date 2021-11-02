from app_arbo import db


class Addarvore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    qtd = db.Column(db.Integer, nullable=False)
    origem = db.Column(db.String(80), nullable=False)
    
    praca_id = db.Column(db.Integer, db.ForeignKey('praca.id'),nullable=False)
    praca = db.relationship('Praca', backref=db.backref('pracas', lazy=True))

    arvore_id = db.Column(db.Integer, db.ForeignKey('arvore.id'),nullable=False)
    arvore = db.relationship('Arvore', backref=db.backref('arvores', lazy=True))

    familia_id = db.Column(db.Integer, db.ForeignKey('familia.id'),nullable=False)
    familia = db.relationship('Familia', backref=db.backref('familias', lazy=True))

    def __repr__(self):
        return '<Addarvore %r>' % self.name


class Arvore (db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(30),nullable=False,unique=True)
    especie=db.Column(db.String(100),nullable=False,unique=True) #teste

class Familia(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(30),nullable=False,unique=True)

class Praca(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(30),nullable=False,unique=True)
    end=db.Column(db.String(100),nullable=False,unique=True) #teste




db.create_all()