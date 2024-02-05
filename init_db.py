from flask import Flask
from models import db , Tarjeta

app= Flask('app')

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
with app.app_context():
    db.create_all()

with app.app_context():
    tarjeta1 = Tarjeta(nombre_producto = "STRUCTURED WIDE LEG SWEATPANTS - SOFT PINK", precio_producto = 340000, url_image = "/static/imagen1.png")
    tarjeta2 = Tarjeta(nombre_producto = "SLIP-ON MICRO-RIBBED MAXI DRESS - SOFT PINK", precio_producto = 575000, url_image = "/static/imagen2.png")
    tarjeta3 = Tarjeta(nombre_producto = "SCOOPED MICRO-RIBBED MAXI DRESS - SOFT PINK", precio_producto = 600000, url_image = "/static/imagen3.png")
    tarjeta4 = Tarjeta(nombre_producto = "BUTTON UP MICRO-RIBBED ROMPER - SOFT PINK", precio_producto = 310000, url_image = "/static/imagen4.png")
    tarjeta5 = Tarjeta(nombre_producto = "T-SHAPE MICRO-RIBBED TANK TOP - SOFT PINK", precio_producto = 210000, url_image = "/static/imagen5.png")
    tarjeta6 = Tarjeta(nombre_producto = "CLASSIC MICRO-RIBBED BOXER - SOFT PINK", precio_producto = 230000, url_image = "/static/imagen6.png")
    tarjeta7 = Tarjeta(nombre_producto = "KEY ZIP-UP CROPPED HOODIE - SOFT PINK", precio_producto = 280000, url_image = "/static/imagen7.png")
    tarjeta8 = Tarjeta(nombre_producto = "STRING CROSSBACK MINI DRESS - SOFT PINK", precio_producto = 480000, url_image = "/static/imagen8.png")
    

  
    db.session.add(tarjeta1)
    db.session.add(tarjeta2)
    db.session.add(tarjeta3)
    db.session.add(tarjeta4)
    db.session.add(tarjeta5)
    db.session.add(tarjeta6)
    db.session.add(tarjeta7)
    db.session.add(tarjeta8)

    db.session.commit()
