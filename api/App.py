from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db = SQLAlchemy(app)


class Products(db.Model):
    __tablename__ = 'Productos'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    nombre = db.Column(db.String(255), nullable=False)
    precio = db.Column(db.String(255), nullable=False)

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __repr__(self):
        return f"<Product {self.nombre}>"

    #db.create_all()


#SELECT FOR ID
@app.route('/product?id=<id>', methods=['GET'])
def get_product(id):
    product = Products.query.get(id)
    del product.__dict__['_sa_instance_state']
    return jsonify(product.__dict__)


@app.route('/products', methods=['GET'])
def get_products():
    productList = []
    for productItem in db.session.query(Products).all():
        del productItem.__dict__['_sa_instance_state']
        productList.append(productItem.__dict__)
    return jsonify(productList)


@app.route('/add?nombre=<nombre>;precio=<precio>', methods=['GET'])
def create_item(nombre, precio):
    db.session.add(Products(nombre, precio))
    db.session.commit()
    return f'Product {nombre} created'


@app.route('/update?id=<id>;nombre=<nombre>;precio=<precio>',
           methods=['GET', 'PUT'])
def update_item(idUpdate, nombre, precio):
    body = request.get_json()
    db.session.query(Products).filter_by(id=idUpdate).update(
        dict(nombre, precio))
    db.session.commit()
    return f"Product [{idUpdate}] {nombre} updated"


@app.route('/delete?id=<id>', methods=['GET', 'DELETE'])
def delete_item(idDelete):
    db.session.query(Products).filter_by(id=idDelete).delete()
    db.session.commit()
    return f"Product [{idDelete}] deleted"


@app.route('/', methods=['GET'])
def hello_word():
    return ""
