from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL


class GroceryStoreForm(FlaskForm):
    """Form for adding/updating a GroceryStore."""
    title = StringField('name', validators=[
                        DataRequired(), Length(min=3, max=80)])
    address = StringField('address', validators=[
                          DataRequired(), Length(min=3, max=80)])
    submit = SubmitField('Submit')


class GroceryItemForm(FlaskForm):
    """Form for adding/updating a GroceryItem."""
    name = StringField('name of Item', validators=[
                       DataRequired(), Length(min=1, max=80)])
    price = FloatField('price of Item')
    category = SelectField('category', choices=ItemCategory.choices())
    photo_url = StringField('photo of item', validators=[require_tld=True, message=None])
    store = QuerySelectField('store', query_factory=lamda: GroceryStore.query)
    submit = SubmitField('Submit')
