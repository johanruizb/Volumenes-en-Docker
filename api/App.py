from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)
print(os.environ['DATABASE_URL'])
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)


class Products(db.Model):
    __tablename__ = 'productos'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    nombre = db.Column(db.String(255), nullable=False)
    precio = db.Column(db.String(255), nullable=False)

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __repr__(self):
        return 'Clase productos'


db.create_all()
db.session.commit()


@app.route('/', methods=['GET'])
def home():
    return 'Home page'


# SELECT FOR ID
@app.route('/product', methods=['GET'])
def get_product():
    id = request.args.get('id')
    product = Products.query.get(id)
    del product.__dict__['_sa_instance_state']
    return jsonify(product.__dict__)


# SELECT ALL
@app.route('/products', methods=['GET'])
def get_products():
    productList = []
    for productItem in db.session.query(Products).all():
        del productItem.__dict__['_sa_instance_state']
        productList.append(productItem.__dict__)
    return jsonify(productList)


# ADD PRODUCT
@app.route('/add', methods=['POST', 'GET'])
def create_item():
    print(request.args.get('nombre'))
    nombre = request.args.get('nombre')
    precio = request.args.get('precio')
    db.session.add(Products(nombre, precio))
    db.session.commit()
    message = f'The data for sock {nombre} has been submitted.'
    return message


# UPDATE PRODUCT
@app.route('/update/<int:id>', methods=['GET', 'PUT'])
def update_item(id):
    nombre = request.args.get('nombre').upper()
    precio = request.args.get('precio')

    product = Products.query.filter_by(id=id).first()
    product.nombre = nombre
    product.precio = precio
    db.session.commit()
    return f'Product [{id}] {nombre} updated'


# DELETE PRODUCT
@app.route('/delete', methods=['GET', 'DELETE'])
def delete_item():
    id = request.args.get('id')
    db.session.query(Products).filter_by(id=id).delete()
    db.session.commit()
    return f'Product [{id}] deleted'
