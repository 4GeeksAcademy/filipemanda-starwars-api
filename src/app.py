"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User , Fav, Character , Planets
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def get_all_user():

    all_user = User.query.all()
    response_body = list(map(lambda x: x.serialize(), all_user))


    return jsonify(response_body), 200

@app.route('/planets', methods=['GET'])
def get_all_planets():

    all_planets = User.query.all()
    response_body = list(map(lambda x: x.serialize(), all_planets))


    return jsonify(response_body), 200


@app.route('/favorites/<id>', methods=['GET'])
def get_single_favorite(id):
    # get a favorite by the user id
    all_faves = Fav.query.filter_by(user_id=id).all()
    print("all faves!!")
    print(all_faves)
    response_body = list(map(lambda fav: fav.serialize(), all_faves))

    return jsonify(response_body), 200

@app.route('/user/<email_in>', methods=['GET'])
def get_single_user(email_in):
    single_user = User.query.filter_by(email = email_in).first()
    if single_user: 
        print("single_user")
        print(single_user)
        result = single_user.serialize()
        return jsonify(result), 200
    else :
        return "user does not exist", 404

@app.route('/characters', methods=['GET'])
def get_all_chars():

    all_user = Character.query.all()
    response_body = list(map(lambda x: x.serialize(), all_user))
    return jsonify(response_body), 200

@app.route('/favorites', methods=['GET'])
def get_all_favortires():

    all_favorites = User.query.all()
    response_body = list(map(lambda x: x.serialize(), all_favorites))


    return jsonify(response_body), 200





# this only runs if `$ python src/app.py` is executed
@app.route('/favorites/<id>', methods=['POST'])
def post_favorite(id):
    new_favorite = request.json
    favorite = Fav(user_id=new_favorite['user_id'], entity_type=new_favorite['entity_type'], name=new_favorite['name'], entity_id=id)
    db.session.add(favorite)
    db.session.commit()

    return jsonify(new_favorite), 200



@app.route('/favorites/<id>', methods=['DELETE'])
def delete_favorite(id):
    # new_favorite = request.json
    favorite = Fav.query.get(id)
    db.session.delete(favorite)
    db.session.commit()

    return jsonify(f'delete'), 200





# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
