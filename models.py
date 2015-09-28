from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
import sqlalchemy
import os

app = Flask(__name__)

file_path = os.path.abspath(os.getcwd())+'/models.db'

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+file_path

db = SQLAlchemy(app)

class Materials(db.Model):
	material = db.Column(db.String(10), primary_key = True)
	description = db.Column(db.String(20))
	category = db.Column(db.String(20))

	def __init__(self, material, description, category):
		self.material = material
		self.description = description
		self.category = category

	def __repr__(self):
		return '%s,%s,%s' % (self.material, self.description, self.category)

db.create_all()