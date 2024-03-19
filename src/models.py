from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    username = db.Column(db.String(), unique=False, nullable=False)
    
    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    
class Planets(db.Model):
   
    id = db.Column(db.Integer,unique=False, nullable=False, primary_key=True)
    planet_name = db.Column(db.String(250),unique=False, nullable=False)
    characters= db.Column(db.Integer(), db.ForeignKey('character.id'), unique=False, nullable=False)

    def __repr__(self):
        return '<Planets %r>' % self.planets_name

    def serialize(self):
        return {
            "id": self.id,
            "planets_name": self.planets_name,
            "user_id" : self.user_id
            # do not serialize the password, its a security breach
        }
    
class Character(db.Model):
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=True)
    height = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    hair_color = db.Column(db.String(200), nullable=False)
    eye_color = db.Column(db.String(200), nullable=False)
    birth_year = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(200), nullable=False)
    homeworld = db.Column(db.String(200), nullable=False)
    # planets_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    # fav_id = db.Column(db.String(), db.ForeignKey('fav.id'))


    def __repr__(self):
        return '<Character %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name
            # do not serialize the password, its a security breach
        }
    
class Fav(db.Model):
    
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    name = db.Column(db.String(), nullable=False)
    entity_type = db.Column(db.String(), nullable=False)
    entity_id = db.Column(db.Integer)
    
    # user = db.relationship('User') 
    # Character = db.relationship('Characters')
    # planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    # planets = db.relationship('Planets')
    

    def __repr__(self):
        return '<Fav %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "user_id": self.user_id,
            "entity_type": self.entity_type,
            "entity_id": self.entity_id
            # do not serialize the password, its a security breach
        }
    