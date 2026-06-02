from Gen_Taref import database
from datetime import datetime

class Usuario(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String , nullable=False)
    email = database.Column(database.String, nullable=False , unique=True)
    senha = database.Column(database.String, nullable=False)
    senha = database.Column(database.String,nullable=False)
    cargo = database.Column(database.String, nullable=False)

class Tarefa(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    id_responsavel = database.Column(database.Integer, database.ForeignKey('usuario.id'))
    id_criador = database.Column(database.Integer, database.ForeignKey('usuario.id'))
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
    data_entrega = database.Column(database.DateTime, nullable=False)
    prazo = database.Column(database.DateTime, nullable=False)
    status = database.Column(database.String, nullable=False)
    demanda = database.Column(database.String, nullable=False)