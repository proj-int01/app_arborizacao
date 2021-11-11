from flask import redirect , render_template, url_for, flash, request, session

from .forms import Addpraca, Addtree 
from app_arbo import db, app
from .models import Familia, Praca, Addarvore, Arvore

@app.route('/')
def home():
    pracas = Praca.query.all()
    return render_template('/trees/index.html', title='Praças de Monte Alto - SP', pracas=pracas)

@app.route('/sobre')
def sobre():
    pracas = Praca.query.all()
    return render_template('sobre.html', pracas=pracas)

@app.route('/search',methods=['GET','POST'])
def search():
     
    if request.method == "POST":
        pracas = Praca.query.all()
        form = request.form
        search_value = form['search_string']
        search = '%{0}%'.format(search_value)
        arvores = Addarvore.query.join(Arvore, Praca ).add_columns(Arvore.id, Arvore.name, Arvore.especie, Praca.id, Praca.name.label('praca'), Addarvore.origem, Addarvore.qtd).filter(Arvore.name.like(search)).all()
     
        return render_template('pesquisar.html', arvores=arvores, pracas=pracas, title='Resultado da pesquisa')
    else:
        return redirect('/')

@app.route('/praca/<int:id>')
def get_praca(id):
    pracas = Praca.query.all()
    get_npraca = Praca.query.filter_by(id=id)
    get_image = Praca.query.filter_by(id=id)
    get_praca = Addarvore.query.filter_by(praca_id=id)
    
    return render_template('/trees/praca.html', pracas=pracas, get_praca=get_praca, get_npraca=get_npraca, get_image=get_image, title='Praças de Monte Alto - SP')

@app.route('/addfamilia', methods=['GET','POST'])
def addfamilia():
    if 'email' not in session:
        flash(f'Favor faça seu login no sistema.', 'success')
        return redirect(url_for('login'))

    if request.method == "POST":
        getfamilia = request.form.get('familia')
        familia = Familia (name=getfamilia)
        db.session.add(familia)
        flash (f'A família {getfamilia} foi cadastrada com sucesso', 'success')
        db.session.commit()
        return redirect(url_for('familias'))
    return render_template('/trees/cadarvore.html', title='Adicionar Famílias')

@app.route('/updatefamilia/<int:id>', methods=['GET','POST'])
def updatefamilia(id):
    if 'email' not in session:
        flash(f'Favor faça seu login no sistema.', 'success')
        return redirect(url_for('login'))
    updatefamilia = Familia.query.get_or_404(id)
    familia = request.form.get('familia')
    if request.method =='POST':
        updatefamilia.name = familia
        flash (f'A família foi atualizada com sucesso', 'success')
        db.session.commit()
        return redirect(url_for('familias'))
    return render_template('/trees/updatefamilia.html', title="Atualizar Família", updatefamilia=updatefamilia)

@app.route('/updatearvore/<int:id>', methods=['GET', 'POST'])
def updatearvore(id):
    if 'email' not in session:
        flash(f'Favor faça seu login no sistema.', 'success')
        return redirect(url_for('login'))
    updatearvore = Arvore.query.get_or_404(id)
    arvore = request.form.get('arvore')
    especie = request.form.get('especie')
    
    if request.method =='POST':
        updatearvore.name = arvore
        updatearvore.especie = especie
        flash (f'A Árvore foi atualizada com sucesso', 'success')
        db.session.commit()
        return redirect(url_for('arvores'))
    return render_template('/trees/updatearvore.html', title='Atualizar Árvore', updatearvore=updatearvore)

@app.route('/addarvore', methods=['GET', 'POST'])
def addarvore():
    if 'email' not in session:
        flash(f'Favor faça seu login no sistema.', 'success')
        return redirect(url_for('login'))
    arvores = Arvore.query.order_by(Arvore.name).all()
    familias = Familia.query.order_by(Familia.name).all()
    pracas = Praca.query.all()
    form = Addtree(request.form)
    if request.method=="POST":
        arvore = request.form.get('arvore')
        familia = request.form.get('familia')
        pracas = request.form.get('praca')
        qtd = form.qtd.data
        origem = form.origem.data

        addarv = Addarvore(qtd=qtd,origem=origem, arvore_id=arvore,familia_id=familia, praca_id=pracas)
        db.session.add(addarv)
        flash(f'A Árvore foi cadastrada com sucesso', 'success')
        db.session.commit()
        return redirect(url_for('admin'))
       
    return render_template('/trees/addarvore.html', title="Cadastrar Árvores", form=form, arvores=arvores, familias=familias, pracas=pracas)

@app.route('/updateaddarvore/<int:id>', methods=['GET', 'POST'])
def updateaddarvore(id):
    if 'email' not in session:
        flash(f'Favor faça seu login no sistema.', 'success')
        return redirect(url_for('login'))
    
    form = Addtree(request.form)
    arvores = Arvore.query.order_by(Arvore.name).all()
    familias = Familia.query.all()
    pracas = Praca.query.all()
    add_arvore = Addarvore.query.get_or_404(id)
    arvore = request.form.get('arvore')
    familia = request.form.get('familia')
    praca = request.form.get('praca')
    
    if request.method=="POST":
        add_arvore.praca_id = praca
        add_arvore.familia_id = familia
        add_arvore.arvore_id = arvore
        add_arvore.qtd = form.qtd.data
        add_arvore.origem = form.origem.data

        db.session.commit()
        flash(f'A relação foi atualizada com sucesso', 'success')
        return redirect(url_for('admin'))

    form.qtd.data = add_arvore.qtd
    form.origem.data = add_arvore.origem

    return render_template('/trees/updateaddarvore.html', title="Cadastrar Árvores", form=form, arvores=arvores, familias=familias, pracas=pracas, add_arvore=add_arvore)

@app.route('/addpraca', methods=['GET', 'POST'])
def addpraca():
    if 'email' not in session:
        flash(f'Favor faça seu login no sistema.', 'success')
        return redirect(url_for('login'))
    if request.method == "POST":
        getpraca = request.form.get('praca')
        getend = request.form.get('end')
        getdesc = request.form.get('desc')
        getimage_1 = request.form.get('image_1')
        getimage_2 = request.form.get('image_2')
        getimage_3 = request.form.get('image_3')
        
        praca = Praca(name=getpraca,end=getend,image_1=getimage_1,image_2=getimage_2,image_3=getimage_3,desc=getdesc)
        db.session.add(praca)
        db.session.commit()
        flash(f'A Praça {getpraca} foi cadastrada com sucesso', 'success')
        return redirect(url_for('pracas'))
    return render_template('/trees/addpraca.html', title='Cadastrar Praças')
  
@app.route('/updatepraca/<int:id>', methods=['GET', 'POST'])
def updatepraca(id):
    if 'email' not in session:
        flash(f'Favor faça seu login no sistema.', 'success')
        return redirect(url_for('login'))
    updatepraca = Praca.query.get_or_404(id)
    praca = request.form.get('praca')
    end = request.form.get('end')
    desc = request.form.get('desc')
    image_1 = request.form.get('image_1')
    image_2 = request.form.get('image_2')
    image_3 = request.form.get('image_3')
    
    if request.method =='POST':
        updatepraca.name = praca
        updatepraca.end = end
        updatepraca.desc = desc
        updatepraca.image_1 = image_1
        updatepraca.image_2 = image_2
        updatepraca.image_3 = image_3
        flash (f'A Praca foi atualizada com sucesso', 'success')
        db.session.commit()
        return redirect(url_for('pracas'))
    return render_template('/trees/updatepraca.html', title='Atualizar praça',updatepraca=updatepraca)

@app.route('/cadarvore', methods=['GET', 'POST'])
def cadarvore():
    if 'email' not in session:
        flash(f'Favor faça seu login no sistema.', 'success')
        return redirect(url_for('login'))  

    if request.method == "POST":
        getarvore = request.form.get('arvore')
        getespecie= request.form.get('especie')
        arvore = Arvore(name=getarvore,especie=getespecie,)
        db.session.add(arvore)
        db.session.commit()
        flash(f'A Árvore {getarvore} foi cadastrada com sucesso', 'success')
        return redirect(url_for('arvores'))
    return render_template('/trees/cadarvore.html', title='Cadastrar Árvores', arvore='arvore')

@app.route('/deletarfamilia/<int:id>', methods=['GET','POST'])
def deletarfamilia(id):
    if 'email' not in session:
        flash(f'Favor faça seu login no sistema.', 'success')
        return redirect(url_for('login'))

    familia = Familia.query.get_or_404(id)
    if request.method =='POST':
        db.session.delete(familia)
        db.session.commit()
        flash (f'A família {familia.name} foi excluída com sucesso', 'success')
        return redirect(url_for('familias'))
    flash (f'A família {familia.name} naõ moi excluída com sucesso', 'success')
    return redirect(url_for('familias'))
   
   
@app.route('/deletarpraca/<int:id>', methods=['GET','POST'])
def deletarpraca(id):
    praca = Praca.query.get_or_404(id)
    if request.method =='POST':
        db.session.delete(praca)
        db.session.commit()
        flash (f'A Praça {praca.name} foi excluída com sucesso', 'success')
        return redirect(url_for('pracas'))
    flash (f'A Praça {praca.name} não foi excluída com sucesso', 'success')
    return redirect(url_for('pracas'))
  
    
@app.route('/deletararvore/<int:id>', methods=['GET','POST'])
def deletararvore(id):
    arvore = Arvore.query.get_or_404(id)
    if request.method =='POST':
        db.session.delete(arvore)
        db.session.commit()
        flash (f'A árvore {arvore.name} foi excluída com sucesso', 'success')
        return redirect(url_for('arvores'))
    flash (f'A árvore {arvore.name} não foi excluída com sucesso', 'success')
    return redirect(url_for('arvores'))

         
@app.route('/deletarrelacao/<int:id>', methods=['GET','POST'])
def deletarrelacao(id):
    arvore = Addarvore.query.get_or_404(id)
    if request.method =='POST':
        db.session.delete(arvore)
        db.session.commit()
        flash (f'O relacionamento foi excluído com sucesso', 'success')
        return redirect(url_for('admin'))
    flash (f'A relacionamento não foi excluido!!', 'success')
    return redirect(url_for('admin'))

