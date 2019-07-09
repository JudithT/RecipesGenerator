import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import BigInteger, Text

db = SQLAlchemy()

class Ingredient(db.Model):
    """Ingredients model"""

    __tablename__ = "ingredients"
    ingredient_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    ingredient_classification = db.Column(db.String(100), nullable=False)
    ingredient_name = db.Column(db.String, nullable=False)

    recipes = db.relationship("IngredientRecipe",
                              backref="ingredients_recipes")
    def __repr__(self):
        return '<Ingredients ingredient_id={} ingredient_classification={} ingredient_name={}>'.format(
            self.ingredient_id,
            self.ingredient_classification,
            self.ingredient_name
        )


class IngredientRecipe(db.Model):
    """Ingredients-recipes"""

    __tablename__ = "ingredients_recipes"
     
    ingredientrecipe_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredients.ingredient_id'), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.recipe_id'), nullable=False)


class Recipe(db.Model):
    """ Recipes"""

    __tablename__ = "recipes"

    recipe_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    instructions = db.Column(Text, nullable=False)
    dishtype = db.Column(db.String(500), nullable=True)
    preparation_time = db.Column(db.Integer, nullable=True)
    recipe_origin = db.Column(db.String(55), nullable=True)
    recipe_name = db.Column(db.String(55), nullable=False)
    image = db.Column(db.String(500), nullable=False)
    
    # ingredients_list: list of Ingredient objects (the ingredients used to make recipe)
    # favorited_by: list of User objects that have favorited this recipe


    def __repr__(self):
        return '<Recipes recipe_id={} instructions={} dishtype={} preparation_time={} recipe_origin={}>'.format(
            self.recipe_id,
            self.instructions,
            self.dishtype,
            self.preparation_time,
            self.recipe_origin
        )



class UserFavoriteRecipe(db.Model):
    """User_Recipe"""

    __tablename__ = "users_favorite_recipes"

    userfavoriterecipe_id = db.Column(db.Integer,primary_key=True, nullable=False, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    recipe_id = db.Column(BigInteger, db.ForeignKey('recipes.recipe_id'), nullable=False)

    def __repr__(self):
        return '<UserFavoriteRecipe userfavoriterecpie_id={} user_id={} recipe_id={}>'.format(
            self.userfavoriterecpie_id,
            self.user_id,
            self.recipe_id
        )


class User(db.Model):
    """User"""

    __tablename__ = "users"
    
    user_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    fname = db.Column(db.String(200), nullable=False)
    lname = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200), nullable=False)

    # List of Recipe objects
    favorites = db.relationship("UserFavoriteRecipe",
                                    backref="users")

    def __repr__(self):
        return '<User user_id={} fname={} lname={} email={} password={}>'.format(
            self.user_id, self.fname, self.lname, self.email, self.password
        )



class UserIngredient(db.Model):
    """Ingredients_users"""

    __tablename__ = "users_ingredients"

    useringredient_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredients.ingredient_id'), nullable=False)

    def __repr__(self):
            return '<UserIngredient useringredient_id={}>'.format(self.useringredient_id)

    
def connect_to_db(app):
    """Connect to database."""

    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or 'postgresql:///recipes'
    app.config['SQLALCHEMY_ECHO'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)