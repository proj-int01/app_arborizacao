from flask import redirect , render_template, url_for, flash, request, session

from .forms import Addpraca, Addtree 
from app_arbo import db, app
from .models import Familia, Praca, Addarvore, Arvore

@app.route('/addfamilia', methods=['GET','POST'])
def addfamilia():
    if request.method == "POST":
        getfamilia = request.form.get('familia')
        familia = Familia (name=getfamilia)
        db.session.add(familia)
        flash (f'A família {getfamilia} foi cadastrada com sucesso', 'success')
        db.session.commit()
        return redirect(url_for('addfamilia'))
    return render_template('/trees/cadarvore.html')


@app.route('/cadarvore', methods=['GET', 'POST'])
def cadarvore():
    if 'email' not in session:
        flash(f'Favor faça seu login no sistema.', 'success')
        return redirect(url_for('login'))    
    if request.method == "POST":
        getarvore = request.form.get('arvore')
        getespecie= request.form.get('especie')
        arvore = Arvore(name=getarvore,especie=getespecie)
        db.session.add(arvore)
        db.session.commit()
        flash(f'A Árvore {getarvore} foi cadastrada com sucesso', 'success')
        return redirect(url_for('cadarvore'))
    return render_template('/trees/cadarvore.html', arvore='arvore')


@app.route('/addarvore', methods=['GET', 'POST'])
def addarvore():
    if 'email' not in session:
        flash(f'Favor faça seu login no sistema.', 'success')
        return redirect(url_for('login'))
    arvores = Arvore.query.all()
    familias = Familia.query.all()
    pracas = Praca.query.all()
    form = Addtree(request.form)
    if request.method=="POST":
        arvore = request.form.get('arvore')
        familia = request.form.get('familia')
        praca = request.form.get('praca')
        qtd = form.qtd.data
        origem = form.origem.data

        addarv = Addarvore(qtd=qtd,origem=origem, arvore_id=arvore,familia_id=familia, praca_id=praca)
        db.session.add(addarv)
        flash(f'A Árvore foi cadastrada com sucesso', 'success')
        db.session.commit()
        return redirect(url_for('admin'))
       
    return render_template('/trees/addarvore.html', title="Cadastrar Árvores", form=form, arvores=arvores, familias=familias, pracas=pracas)


@app.route('/addpraca', methods=['GET', 'POST'])
def addpraca():
    if 'email' not in session:
        flash(f'Favor faça seu login no sistema.', 'success')
        return redirect(url_for('login'))
    if request.method == "POST":
        getpraca = request.form.get('praca')
        getend = request.form.get('end')
        praca = Praca(name=getpraca,end=getend)
        db.session.add(praca)
        db.session.commit()
        flash(f'A Praça {getpraca} foi cadastrada com sucesso', 'success')
        return redirect(url_for('addpraca'))
    return render_template('/trees/addpraca.html')
    
    
    
    #form = Addpraca(request.form)
    #return render_template('/trees/addpraca.html', title="Cadastrar Praças/Fotos", form=form)