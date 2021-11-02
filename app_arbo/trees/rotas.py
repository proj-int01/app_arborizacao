from flask import redirect , render_template, url_for, flash, request

from .forms import Addtree, Addpraca
from app_arbo import db, app
from .models import Family, Arvore, Praca 

@app.route('/addfamilia', methods=['GET','POST'])
def addfamilia():
    if request.method == "POST":
        getfamily = request.form.get('family')
        family = Family (name=getfamily)
        db.session.add(family)
        flash (f'A family {getfamily} foi cadastrada com sucesso', 'success')
        db.session.commit()
        return redirect(url_for('addfamilia'))
    return render_template('/trees/cadarvore.html')


@app.route('/cadarvore', methods=['GET', 'POST'])
def cadarvore():    
    if request.method == "POST":
        getarvore = request.form.get('arvore') #,'especie')
        getespecie= request.form.get('especie')
        arvore = Arvore (name=getarvore,especie=getespecie)
        db.session.add(arvore)
        db.session.commit()
        flash(f'A Praça {getarvore} foi cadastrada com sucesso', 'success')
        return redirect(url_for('cadarvore'))
    return render_template('/trees/cadarvore.html', arvore='arvore')


@app.route('/addarvore', methods=['GET', 'POST'])
def addtree():
    arvores = Arvore.query.all()
    familias = Family.query.all()
    pracas = Praca.query.all()
    form = Addtree(request.form)
    return render_template('/trees/addarvore.html', title="Cadastrar Árvores", form=form, arvores=arvores, familias=familias, pracas=pracas)


@app.route('/addpraca', methods=['GET', 'POST'])
def addpraca():
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