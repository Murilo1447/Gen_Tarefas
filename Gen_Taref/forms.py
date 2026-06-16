from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class FormLogin(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired()])
    botao_confirmacao = SubmitField("Logar")


class FormCriarConta(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    nome = StringField("Usuário", validators=[DataRequired()])
    senha = PasswordField("Senha", validators=[DataRequired(), Length(min=6)])
    confirmar_senha = PasswordField("Confirmar Senha", validators=[DataRequired(), EqualTo("senha")])
    cargo = SelectField("Cargo", choices=[("funcionario", "Funcionário"), ("gerente", "Gerente")],
                        validators=[DataRequired()])

    botao_confirmacao = SubmitField("Criar Conta")