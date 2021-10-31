from wtforms import Form, BooleanField, StringField, PasswordField, validators

class RegistrationForm(Form):
    name = StringField('Nome Completo :', [validators.Length(min=4, max=25)])
    username = StringField('Usuário :', [validators.Length(min=4, max=25)])
    email = StringField('Email :', [validators.Length(min=6, max=35)])
    password = PasswordField('Digite a senha', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='As senhas são diferentes')
    ])
    confirm = PasswordField('Digite novamente a senha')
    

class LoginFormulario(Form):
        email = StringField('Email :', [validators.Length(min=6, max=35)])
        password = PasswordField('Digite a senha', [validators.DataRequired()])