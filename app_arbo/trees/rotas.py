from flask import redirect , render_template, url_for, flash, request
from .forms import Addtree, Addgrove2
from app_arbo import db, app
from .models import Family, Grove 

@app.route('/addfamilia', methods=['GET', 'POST'])
def addfamily():
    
    if request.method == "POST":
        getfamily = request.form.get('family')
        family = Family (name=getfamily)
        db.session.add(family)
        db.session.commit()
        flash(f'A family {getfamily} foi cadastrada com sucesso', 'success')
        return redirect(url_for('addfamily'))
    return render_template('/trees/addfamilia.html', familia='familia')





@app.route('/addgrove', methods=['GET', 'POST'])
def addgrove():
    
    if request.method == "POST":
        getgrove = request.form.get('grove')
        grove = Grove (name=getgrove,address=getgrove)
        db.session.add(grove)
        db.session.commit()
        flash(f'A Praça {getgrove} foi cadastrada com sucesso', 'success')
        return redirect(url_for('addgrove'))
    return render_template('/trees/addfamily.html')


@app.route('/addarvore', methods=['GET', 'POST'])
def addtree():
    form = Addtree(request.form)
    return render_template('/trees/addarvore.html', title="Cadastrar Árvores", form=form)


@app.route('/addpraca', methods=['GET', 'POST'])
def addgrove2():
    form = Addgrove2(request.form)
    return render_template('/trees/addpraca.html', title="Cadastrar Praças/Fotos", form=form)