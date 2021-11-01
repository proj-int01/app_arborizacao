from flask import redirect , render_template, url_for, flash, request

from app_arbo import db, app
from .models import Family, Grove 
@app.route('/addfamily', methods=['GET', 'POST'])
def addfamily():
    
    if request.method == "POST":
        getfamily = request.form.get('family')
        family = Family (name=getfamily)
        db.session.add(family)
        db.session.commit()
        flash(f'A family {getfamily} foi cadastrada com sucesso', 'success')
        return redirect(url_for('addfamily'))
    return render_template('/trees/addfamily.html', family='family')





@app.route('/addgrove', methods=['GET', 'POST'])
def addgrove():
    
    if request.method == "POST":
        getgrove = request.form.get('grove')
        grove = Grove (name=getgrove)
        db.session.add(grove)
        db.session.commit()
        flash(f'A Praça {getgrove} foi cadastrada com sucesso', 'success')
        return redirect(url_for('addgrove'))
    return render_template('/trees/addfamily.html')

