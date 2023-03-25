"""Flask app for Cupcakes"""
from flask import Flask, request, jsonify, render_template
from models import db, connect_db, Cupcake
from form import AddCupcakeForm
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.app_context().push()
connect_db(app)
# db.create_all()

from flask_debugtoolbar import DebugToolbarExtension
app.config['SECRET_KEY'] = "SMOKEY"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

@app.route('/')
def index_page():
    """Renders html to list all cupcakes and form"""
    form = AddCupcakeForm()
    return render_template('index.html', form=form)
# *****************************
# RESTFUL TODOS JSON API
# *****************************
@app.route("/api/cupcakes")
def list_cupcakes():
    """Returns JSON of a list of all cupcakes"""

    all_cupcakes = [cc.serialize() for cc in Cupcake.query.all()]
    return jsonify(cupcakes=all_cupcakes)

@app.route("/api/cupcakes/<int:id>")
def get_cupcake(id):
    """Returns a JSON oft the identified cupkcake"""

    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake = cupcake.serialize())


@app.route("/api/cupcakes", methods=["POST"])
def create_cupcake():
    """Return JSON of a newly created cupcake"""
    new_cupcake = Cupcake(
        flavor = request.json['flavor'],
        size = request.json['size'],
        rating = request.json['rating'],
        image = request.json['image'] or None
    )
    db.session.add(new_cupcake)
    db.session.commit()
    resp_json = jsonify(cupcake=new_cupcake.serialize())
    return (resp_json, 201)

@app.route("/api/cupcakes/<int:id>", methods=["PATCH"])
def update_cupcake(id):
    """Updates identified cupkcake and returns JSON of updated info"""

    cupcake = Cupcake.query.get_or_404(id)
    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.rating = request.json.get('rating', cupcake.rating)
    cupcake.image = request.json.get('image', cupcake.image)
    db.session.commit()
    return jsonify(cupcake = cupcake.serialize())

@app.route("/api/cupcakes/<int:id>", methods=["DELETE"])
def delete_cupcake(id):
    """Deletes identified cupkcake"""
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message="Deleted")



#-----------------------POST DATA SAMPLES ---------------------------
# {
# 	"flavor":"Cookies&Cream",
# 	"size":"meduim",
# 	"rating":"9",
# 	"image":"https://thefirstyearblog.com/wp-content/uploads/2017/03/cookies-and-cream-cupcakes-Square1.png"
# }

{
	"flavor":"Carrot",
	"size":"small",
	"rating":"7",
	"image":"https://www.cookingclassy.com/wp-content/uploads/2014/01/carrot_cake_cupcakes2edit..jpg"
}
    
