from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField, DateField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from Gen_Taref.models import Usuario


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



    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError("Email já cadastrado. Faça login para continuar.")



class FormCriarTarefa(FlaskForm):
    titulo = StringField('Título', validators=[DataRequired()])
    descricao = TextAreaField('Descrição', validators=[DataRequired()])
    id_responsavel = IntegerField(
        'Funcionário',
        validators=[DataRequired()]
    )


    data_entrega = DateField('Data de Entrega',format='%Y-%m-%d',validators=[DataRequired()])

    status = SelectField(
        'Status',
        choices=[
            ('Pendente', 'Pendente'),
            ('Em andamento', 'Em andamento'),
            ('Concluída', 'Concluída')
        ],
        default='Pendente'
    )

    demanda = SelectField(
        'Prioridade',
        choices=[
            ('Baixa', 'Baixa'),
            ('Normal', 'Normal'),
            ('Alta', 'Alta'),
            ('Urgente', 'Urgente')
        ],
        default='Normal'
    )

    botao_criar = SubmitField('Criar Tarefa')