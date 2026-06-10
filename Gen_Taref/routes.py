from Gen_Taref import app
from flask import render_template, url_for
from flask_login import login_required
from Gen_Taref.forms import FormLogin, FormCriarConta

@app.route('/', methods=['GET', 'POST'])
def homepage():
    return render_template('homepage.html')

@app.route('/criarconta', methods=['GET', 'POST'])
def criar_conta():
    formcriarconta = FormCriarConta()
    return render_template('criarconta.html')


@app.route('/perfil/<usuario>')
@login_required
def perfil(usuario):
    return render_template('perfil.html', usuario=usuario)
