# import os
from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from database import db, migrate
from schemas import ma
from limiter import limiter
from caching import cache

from models.customer import Customer
from models.order import Order
from models.product import Product
from models.cart import Cart

from routes.customerBP import customer_blueprint
from routes.orderBP import order_blueprint
from routes.productBP import product_blueprint
# from routes.tokenBP import token_blueprint
# from routes.cartBP import cart_blueprint




def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(f'config.{config_name}')

    db.init_app(app)
    ma.init_app(app)
    limiter.init_app(app)
    cache.init_app(app)
    migrate.init_app(app, db)

    return app

def blueprint_config(app):
    app.register_blueprint(customer_blueprint, url_prefix='/customers')
    app.register_blueprint(order_blueprint, url_prefix='/orders')
    app.register_blueprint(product_blueprint, url_prefix='/products')
    # app.register_blueprint(token_blueprint, url_prefix='/token')
    # app.register_blueprint(cart_blueprint, url_prefix='/carts')

def config_rate_limit():
    limiter.limit("100 per day")(customer_blueprint)
    limiter.limit("100 per day")(order_blueprint)
    limiter.limit("100 per day")(product_blueprint)
    # limiter.limit("100 per day")(cart_blueprint)

if __name__ == "__main__":

    app = create_app('DevelopmentConfig')

    blueprint_config(app)
    config_rate_limit()

    with app.app_context():
        db.drop_all()
        db.create_all()

    app.run(debug=True)