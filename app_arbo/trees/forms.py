from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms import Form,IntegerField,StringField,BooleanField,TextAreaField,validators


class Addtree(Form):
    qtd = IntegerField('Quantidade: ', [validators.DataRequired()])
    origem = StringField('Origem: ', [validators.DataRequired()])
       



class Addpraca(Form): # para cadastrar imagem das Praças
    name = StringField('Nome: ', [validators.DataRequired()])
    adress = StringField('Endereço: ', [validators.DataRequired()])
    desc = TextAreaField('Descrição: ', [validators.DataRequired()])

    