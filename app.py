from flask import Flask, render_template, request, redirect, url_for, jsonify
from database_helpers import (
    get_product_by_id,
    add_product,
    register_customer,
    purchase_product
)

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('index.html')



@app.route('/product/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = get_product_by_id(product_id)
    if product is None:
        return jsonify({'error': 'Product not found'}), 404
    return jsonify(product)



@app.route('/product/add', methods=['POST'])
def add_new_product():
    data = request.json
    success = add_product(
        seller_id=data['sellerId'],
        name=data['productName'],
        price=float(data['productPrice']),
        description=data['productDescription']
    )
    if success:
        return jsonify({'message': 'Product added successfully'}), 201
    return jsonify({'error': 'Failed to add product'}), 400



@app.route('/customer/register', methods=['POST'])
def register_new_customer():
    data = request.json
    customer_id = register_customer(
        name=data['customerName'],
        email=data['customerEmail'],
        password=data['customerPassword']
    )
    if customer_id is not None:
        return jsonify({
            'message': 'Customer registered successfully',
            'customerId': int(customer_id)
        }), 201
    return jsonify({'error': 'Failed to register customer'}), 400



@app.route('/purchase', methods=['POST'])
def make_purchase():
    data = request.json
    success = purchase_product(
        customer_id=data['buyerCustomerId'],
        product_id=data['purchaseProductId'],
        quantity=data['quantity']
    )
    if success:
        return jsonify({'message': 'Purchase successful'}), 201
    return jsonify({'error': 'Failed to process purchase'}), 400



if __name__ == '__main__':
    app.run(debug=True)
