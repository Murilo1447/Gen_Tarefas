from flask import render_template, url_for, redirect
from flask_login import login_required, login_user, logout_user, current_user
from Gen_Taref import app, database, bcrypt
from Gen_Taref.forms import FormLogin, FormCriarConta
from Gen_Taref.models import Usuario


@app.route('/', methods=['GET', 'POST'])
def homepage():
    form = FormLogin()
    if form.validate_on_submit():
        usuario = Usuario.query.filter_by(email=form.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, form.senha.data):
            login_user(usuario, remember=True)
            return redirect(url_for('perfil', id_usuario=usuario.id))


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
        return redirect(url_for('perfil', id_usuario=usuario.id))

    return render_template('criarconta.html', form=form)


@app.route('/perfil/<id_usuario>')
@login_required
def perfil(id_usuario):
    if int(id_usuario) == (current_user.id):
        # O usuario está vendo o perfil dele
        return render_template('perfil.html', usuario=current_user)
    else:
        usuario = Usuario.query.get(int(id))
        # Está vendo o perfil de outra pessoa
    return render_template('perfil.html', usuario=usuario)



@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('homepage'))