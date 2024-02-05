from flask_sqlalchemy import SQLAlchemy

db= SQLAlchemy() #instanciamos la base de datos

class Tarjeta(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre_producto = db.Column(db.String(80))
    precio_producto = db.Column(db.Integer)
    url_image = db.Column(db.String(40))

