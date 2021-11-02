from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms import Form,IntegerField,StringField,BooleanField,TextAreaField,validators


class Addtree(Form):
    qtd = IntegerField('Quantidade: ', [validators.DataRequired()])
    origin = StringField('Origem: ', [validators.DataRequired()])
    description = TextAreaField('Descrição: ', [validators.DataRequired()])

    #image_1 = FileField('Imagem 1: ', validators=[FileRequired(),FileAllowed(['jpg', 'png', 'git', 'jpeg'])])
    #image_2 = FileField('Imagem 2: ', validators=[FileRequired(),FileAllowed(['jpg', 'png', 'git', 'jpeg'])])
    



class Addpraca(Form): # para cadastrar imagem das Praças
    name = StringField('Nome: ', [validators.DataRequired()])
    adress = StringField('Endereço: ', [validators.DataRequired()])
    desc = TextAreaField('Descrição: ', [validators.DataRequired()])

    image_1 = FileField('Imagem 1: ', validators=[FileRequired(),FileAllowed(['jpg', 'png', 'git', 'jpeg'])])
    image_2 = FileField('Imagem 2: ', validators=[FileRequired(),FileAllowed(['jpg', 'png', 'git', 'jpeg'])])
    image_3 = FileField('Imagem 3: ', validators=[FileRequired(),FileAllowed(['jpg', 'png', 'git', 'jpeg'])])
    image_4 = FileField('Imagem 4: ', validators=[FileRequired(),FileAllowed(['jpg', 'png', 'git', 'jpeg'])])
