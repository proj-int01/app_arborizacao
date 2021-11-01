from app_arbo import db


class Grove(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(30),nullable=False,unique=True)
    address=db.Column(db.String(100),nullable=True,unique=True) #teste

class Family(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(30),nullable=False,unique=True)

db.create_all()