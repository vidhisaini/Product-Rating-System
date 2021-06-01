from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Product(db.Model):
    product_id = db.Column(db.String(32), primary_key=True)
    total_ratings = db.Column(db.Integer)
    average_ratings = db.Column(db.Integer)

    def __init__(self, product_id, total_ratings, average_ratings):
        self.product_id = product_id
        self.total_ratings = total_ratings
        self.average_ratings = average_ratings


class ProductSchema(ma.Schema):

    class Meta:
        fields = ('product_id', 'total_ratings', 'average_ratings')

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)


class RatingsManager(Resource):

    @staticmethod
    @app.route('/fetch-products', methods=['GET'])
    def get():
        try:
            id = request.args['product_id']
        except Exception as _:
            id = None

        if not id:
            products = Product.query.all()
            return jsonify(products_schema.dump(products))
        product = Product.query.get(id)
        return jsonify(product_schema.dump(product))

    @staticmethod
    @app.route('/rate-product', methods=['PUT'])
    def put():
        try:
            ratingList = request.data
        except Exception as _:
            ratingList = None

        if not ratingList:
            return jsonify({'Message': 'Must provide the product id and rating'})
        jdata = request.get_json()

        try:
            for product in jdata:
                product_id = str(product['product_id'])
                rating = int(product['rating'])
                product = Product.query.get(product_id)
                product.average_ratings = (
                    product.total_ratings * product.average_ratings + rating) / (product.total_ratings + 1)
                product.total_ratings += 1

            db.session.commit()
            return jsonify({
                'Message': 'Ratings updated'
            })
        except Exception as e:
            return jsonify({"Either the format or the information is incorrect ": str(e)})

    @staticmethod
    @app.route('/add-product', methods=['POST'])
    def post():
        try:
            product_id = request.json['product_id']
            total_ratings = request.json['total_ratings']
            average_ratings = request.json['average_ratings']

            if(Product.query.get(product_id)):
                return jsonify({
                    'Message': 'Product already exists!'
                })

            product = Product(product_id, total_ratings, average_ratings)
            db.create_all()
            db.session.add(product)
            db.session.commit()
            return jsonify({
                'Message': 'Product inserted!'
            })
        except Exception as e:
            return jsonify({"Please enter in a correct format": str(e)})


if __name__ == '__main__':

    app.run(debug=True)
