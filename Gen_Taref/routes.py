from flask import render_template, url_for, redirect
from flask_login import login_required, login_user
from Gen_Taref import app, database, bcrypt
from Gen_Taref.forms import FormLogin, FormCriarConta
from Gen_Taref.models import Usuario


@app.route('/', methods=['GET', 'POST'])
def homepage():
    form = FormLogin()
    if form.validate_on_submit():

        pass
    return render_template('homepage.html', form=form)


@app.route('/criarconta', methods=['GET', 'POST'])
def criar_conta():
    form = FormCriarConta()
    if form.validate_on_submit():
        senha_criptografada = bcrypt.generate_password_hash(form.senha.data).decode('utf-8')


        usuario = Usuario(
            nome=form.nome.data,
            email=form.email.data,
            senha=senha_criptografada,
            cargo=form.cargo.data  
        )
        database.session.add(usuario)
        database.session.commit()
        login_user(usuario, remember=True)
        return redirect(url_for('perfil', usuario=usuario.nome))

    return render_template('criarconta.html', form=form)


@app.route('/perfil/<usuario>')
@login_required
def perfil(usuario):
    return render_template('perfil.html', usuario=usuario)