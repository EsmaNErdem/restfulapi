"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db =  SQLAlchemy()

default_img = "https://tinyurl.com/demo-cupcake"

def connect_db(app):
    """Connecting the database"""

    db.app = app
    db.init_app(app)

class Cupcake(db.Model):
    """Creating Ccupcake Model"""

    __tablename__ = "cupcakes"

    id = db.Column(db.Integer,
                   primary_key=True,
                    autoincrement=True)
    flavor = db.Column(db.Text, nullable=False, unique=True)
    size = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.Text, nullable=False, default = default_img)

    def serialize(cc):
        """Serialize a dessert SQLAlchemy obj to dictionary."""

        return {
            "id": cc.id,
            "flavor": cc.flavor,
            "size": cc.size,
            "rating": cc.rating,
            "image": cc.image
        }


    def __repr__(self):
        """Show info"""

        u = self
        return f"<Cupcake id:{u.id} flavor:{u.flavor} size:{u.size} rating:{u.rating}"
