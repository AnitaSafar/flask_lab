from flask import render_template
from app import app
from models.cakes import orders

@app.route('/orders')
def index():
    return render_template('index.html', title="Cake Shop", orders=orders)

@app.route('/orders/<order_number>')
def find_order(order_number):
    return render_template('order.html', title="Cake Shop", item=orders[int(order_number)-1])