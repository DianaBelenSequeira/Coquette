from flask import Flask, render_template, request, redirect, url_for
from models import db, Tarjeta
app = Flask(__name__)
import locale

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

locale.setlocale(locale.LC_ALL, 'es_PY.UTF-8')

@app.route('/')

def index():
    tarjetas = Tarjeta.query.all()
    for tarjeta in tarjetas:
        tarjeta.precio_producto = format_currency(tarjeta.precio_producto)
    return render_template('coquette.html', tarjetas=tarjetas)

def format_currency(value):
    formatted_value= locale.currency(value, grouping=True  ) 
    return formatted_value

@app.route('/producto/nuevo', methods=['GET', 'POST'])
def nuevo_producto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = request.form['precio']
        imagen = request.form['url_image']
        producto = Tarjeta(nombre_producto=nombre, precio_producto=precio, url_image=imagen)
        db.session.add(producto)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('producto_nuevo.html')


@app.route('/producto/editar/<int:id>', methods=['GET', 'POST'])
def editar_producto(id):
    producto = Tarjeta.query.get_or_404(id)
    if request.method == 'POST':
        producto.nombre_producto = request.form['nombre']
        producto.precio_producto = request.form['precio']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('editar_producto.html', producto=producto)

@app.route('/producto/eliminar/<int:id>', methods=['POST'])
def eliminar_producto(id):
    producto = Tarjeta.query.get_or_404(id)
    db.session.delete(producto)
    db.session.commit()
    return redirect(url_for('index'))



if __name__== 'main_':
    app.run (debug=True)