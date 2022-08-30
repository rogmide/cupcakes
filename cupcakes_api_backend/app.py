from shelve import DbfilenameShelf
from flask import Flask, request, redirect, render_template, jsonify
from models import Cupcake, db, connect_db
from _form import AddCupCakeForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "123"

connect_db(app)


@app.route('/')
def show_homepage():
    '''Show home page for the user'''

    cupcake_form = AddCupCakeForm()

    return render_template('home.html', cupcake_form=cupcake_form)


@app.route('/api/cupcakes')
def get_all_cupcakes():
    '''Get all the cupcakes from the db'''

    cupcakes = [Cupcake.serialice(c) for c in Cupcake.query.all()]

    return jsonify(cupcakes=cupcakes)


@app.route('/api/cupcakes/<int:id>')
def get_a_cupcake_by_id(id):
    '''Get a cupcake by id'''

    cupcake = Cupcake.query.get_or_404(id)

    return jsonify(cupcake=cupcake.serialice())


@app.route('/api/cupcakes', methods=['POST'])
def create_cupcake():
    '''Add a new cupcake to db'''

    flavor = request.json["flavor"]
    size = request.json["size"]
    rating = request.json["rating"]
    image = request.json["image"] if request.json["image"] else None

    new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)
    db.session.add(new_cupcake)
    db.session.commit()

    return (jsonify(cupcake=new_cupcake.serialice()), 201)


@app.route('/api/cupcakes/<int:id>', methods=['PATCH'])
def update_cupcake(id):
    '''Update a new cupcake to db'''

    edit_cupcake = Cupcake.query.get_or_404(id)

    edit_cupcake.flavor = request.json["flavor"]
    edit_cupcake.size = request.json["size"]
    edit_cupcake.rating = request.json["rating"]
    edit_cupcake.image = request.json["image"]

    db.session.add(edit_cupcake)
    db.session.commit()

    return (jsonify(cupcake=edit_cupcake.serialice()), 200)


@app.route('/api/cupcakes/<int:id>', methods=['DELETE'])
def delete_cupcake(id):
    '''Delete a new cupcake to db'''

    cupcake = Cupcake.query.get_or_404(id)

    db.session.delete(cupcake)
    db.session.commit()

    return (jsonify({"delete": f"{id} was deleted"}), 200)


@app.route('/api/cupcakes/<search>')
def get_search_by_flavor(search):

    finded_cupcake = Cupcake.query.filter(Cupcake.flavor.ilike(f'{search}%'))
    cupcakes = [Cupcake.serialice(c) for c in finded_cupcake]

    return (jsonify(cupcake=cupcakes), 200)
