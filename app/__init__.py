from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import urllib.parse

# Create the Flask application instance
app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Desertsky%40123@localhost:3306/test'

db = SQLAlchemy(app)

# Define route

from app.routes import user


