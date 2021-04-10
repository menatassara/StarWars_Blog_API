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
from models import db, User, People, Planets, Favorites
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
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
def get_user():

    # response_body = {
    #     "msg": "Hello, this is your GET /user response "
    # }
    user = User.query.all()
    all_users = list(map(lambda x: x.serialize(), User.query))
    return jsonify(all_users), 200

@app.route('/user', methods=['POST'])
def create_user():

    request_body_user = request.get_json()
    newuser = User(user_name=request_body_user["user_name"], email=request_body_user["email"], password=request_body_user["password"],is_active=request_body_user["is_active"])
    db.session.add(newuser)
    db.session.commit()
    return jsonify(request_body_user), 200

@app.route('/user/<int:id>', methods=['GET'])
def get_userid(id):
    userid = User.query.get(id)
    result = userid.serialize()
    return jsonify(result), 200

@app.route('/people', methods=['GET'])
def get_people():

    response_body = {
        "msg": "Eso pipol"
    }
    return jsonify(response_body), 200

@app.route('/people/<int:id>', methods=['GET'])
def get_peopleid(id):
    personid = People.query.get(id)
    result = peopleid.serialize()
    return jsonify(response_body), 200

@app.route('/planets', methods=['GET'])
def get_planets():

    response_body = {
        "msg": "GET de planets"
    }

    return jsonify(response_body), 200

@app.route('/planets/<int:id>', methods=['GET'])
def get_planetsid(id):
    planetsid = Planets.query.get(id)
    result = planetsid.serialize()
    return jsonify(response_body), 200

@app.route('/user/<int:id>/favorites', methods=['GET'])
def get_fav(id):
    query= User.query.get(id)
    if query is None:
        return("wrong")
    else:
        result= Favorites.query.filter_by(user_id= query.id)
        lista = list(map(lambda x: x.serialize(), result))
        return jsonify(lista),200

@app.route('/user/<int:userid>/favorites', methods=['POST'])
def post_fav(userid):
    req = request.get_json()
    fav = Favorites(user_id=userid, planets_id=req["planets_id"])
    db.session.add(fav)
    db.session.commit()
    return("Good")


@app.route('/favorites/<int:favid>', methods=['DELETE'])
def del_fav(favid):
    fav = Favorites.query.get(favid)
    if fav is None:
        raise APIException('Favorites not found', status_code=404)
    db.session.delete(fav)
    db.session.commit()
    return ("Erased")

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)