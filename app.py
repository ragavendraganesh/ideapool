from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_talisman import Talisman
import os

app = Flask(__name__)
Talisman(app, force_https=False)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.getcwd()+'/login-flask-restfull.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['JWT_SECRET_KEY'] = 'sekretu'
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
app.config['JWT_HEADER_NAME'] = 'x-access-token'
app.config['JWT_HEADER_TYPE'] = ''
CORS(app)
api_flask = Api(app)
db = SQLAlchemy(app)
jwt = JWTManager(app)