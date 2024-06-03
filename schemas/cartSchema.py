from marshmallow import fields
from schemas import ma

class CartSchema(ma.Schema):
    id = fields.Integer(required=False)
    customer_id = fields.Integer(required=True)
    product_id = fields.Integer(required=True)
    quantity = fields.Integer(required=True)
    total_price = fields.Integer(required=True)

    class Meta:
        fields = ('id','customer_id','product_id','quantity','total_price')

cart_schema = CartSchema()
carts_schema = CartSchema(many=True)
