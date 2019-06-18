from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class Blogs(db.Model):
	__tablename__="blogs"
	bid=db.Column(db.Integer,primary_key=True)
	heading=db.Column(db.String(200))
	img=db.Column(db.String(50))
	content=db.Column(db.String(60000))