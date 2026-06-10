from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Gen_Taref.db'
app.config['SECRET_KEY']='8776681e7fd816a395d0c64ad3aa517b38b3522ebfea12e66d49a4fe44406aa7'
database = SQLAlchemy(app)
Bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'homepage'


from Gen_Taref import routes, models