"""Form Models for Cupcake Add Form"""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField
from wtforms.validators import InputRequired, NumberRange, URL

class AddCupcakeForm(FlaskForm):
    """Forms for adding cupcakes"""

    flavor = StringField("Flavor",
                         validators=[InputRequired()],)

    size = StringField("Size",
                         validators=[InputRequired()],) 
    rating = FloatField("Rating", 
                        validators=[InputRequired(), NumberRange(min=1.0, max=10.0, message="Rating must be between 1 and 10.")], )
    image = StringField("Photo URL",
                       validators=[InputRequired(), URL()],)    
