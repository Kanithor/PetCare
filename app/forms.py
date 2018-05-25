from wtforms import Form
from wtforms import StringField, IntegerField, validators

class NewPet(Form):
    name = StringField('Nombre')
    race = StringField('Raza')
    size = StringField('Tamaño')
    colour = StringField('Color')

