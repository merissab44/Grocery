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

    # TODO: Add the following fields to the form class:
    # - name - StringField
    # - price - FloatField
    # - category - SelectField (specify the 'choices' param)
    # - photo_url - StringField (use a URL validator)
    # - store - QuerySelectField (specify the `query_factory` param)
    # - submit button
    pass
