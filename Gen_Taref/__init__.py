from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Gen_Taref.db'
database = SQLAlchemy(app)

from Gen_Taref import routes, models