from flask import render_template, session, request, redirect, url_for, flash
from app_arbo.trees.models import Addarvore, Praca, Familia, Arvore
from app_arbo import app, db, bcrypt

from .models import User 
from .forms import RegistrationForm, LoginFormulario
import os


@app.route('/admin')
def admin():
    if 'email' not in session:
        flash(f'Favor faça seu login no sistema.', 'success')
        return redirect(url_for('login'))
    arvores = Addarvore.query.all()
    return render_template('admin/index.html', title='Página Administrativa', arvores=arvores)

@app.route('/pracas')
def pracas():
    if 'email' not in session:
        flash(f'Favor faça seu login no sistema.', 'success')
        return redirect(url_for('login'))
    pracas = Praca.query.order_by(Praca.id.desc()).all()
    return render_template('admin/pracas.html', title='Página Praças', pracas=pracas)

@app.route('/arvores')
def arvores():
    if 'email' not in session:
        flash(f'Favor faça seu login no sistema.', 'success')
        return redirect(url_for('login'))
    arvores = Arvore.query.order_by(Arvore.id.desc()).all()
    return render_template('admin/arvores.html', title='Página Árvores', arvores=arvores)

@app.route('/familias')
def familias():
    if 'email' not in session:
        flash(f'Favor faça seu login no sistema.', 'success')
        return redirect(url_for('login'))
    familias = Familia.query.order_by(Familia.id.desc( )).all()
    return render_template('admin/familia.html', title='Página Famílias', familias=familias)

@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    if 'email' not in session:
        flash(f'Favor faça seu login no sistema.', 'success')
        return redirect(url_for('login'))
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(name=form.name.data, username=form.username.data, email=form.email.data, password=hash_password)
        db.session.add(user)
        db.session.commit()

        flash(f'{form.name.data} Registrado com sucesso!', 'success')
        return redirect(url_for('login'))
    return render_template('admin/registrar.html', title='Página de Registro', form=form)


@app.route('/login',methods=['GET', 'POST'])
def login():
    form=LoginFormulario(request.form)
    if request.method == "POST" and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['email'] = form.email.data
            flash(f'Olá {form.email.data} Você está logado', 'success')
            return redirect(request.args.get('next')or url_for('admin'))
        else:
            flash(f'Não foi fazer o login no sistema.', 'danger')

    return render_template('admin/login.html', form=form, title='Página de Login')




    