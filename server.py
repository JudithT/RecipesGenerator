""" Recipe Generator"""
from jinja2 import StrictUndefined
from flask import (Flask, render_template,redirect,request,flash, session)
# from flask_debugtoolbar import DebugToolbarExtension
from model import User, connect_to_db, db, Recipe,UserFavoriteRecipe

import requests

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails
# silently. This is horrible. Fix this so that, instead, it raises an
# error.
app.jinja_env.undefined = StrictUndefined



# RECIPE_TOKEN = os.environ.get('RECIPE_TOKEN')

# RECIPEBASEDINGREDIENTS_URL = "https://www.eventbriteapi.com/v3/"

# USER_ID = "Your-User-Id-Here"


@app.route('/')
def index():
    """Index page"""
    return render_template("index.html")


@app.route('/signin')
def signinForm():
    """Sign in Page"""
    return render_template("signIn.html")


@app.route('/signin', methods=["POST"])
def processlogin():
    password = request.form.get("password")
    email=request.form.get("email")
    user=User.query.filter_by(email=email, password=password).first()
    print("USER======",user)

    if user:
        session['user_id'] = user.user_id
        flash("Successful Login")
        return redirect('/homepage')
    else:
        return redirect('/signin')



@app.route("/register",methods=["GET"])
def register_form():
    """ Registration"""
    return render_template("signUp.html")



@app.route('/homepage')
def homepage():
    """Homepage"""

    return render_template("homepage.html")


@app.route('/processRegister', methods=["POST"])
def register_process():
    fname= request.form.get("fname")
    lname=request.form.get("lname")
    email=request.form.get("email")
    password=request.form.get("password")

    user_email = User.query.filter_by(email=email).first()
    
    if user_email != None:
        flash("You registered already, please proceed to sign in page")
        return redirect('/signin')
    else:
        flash("Successful registration")
        user=User(fname=fname,lname=lname, email=email, password= password)
        db.session.add(user)
        db.session.commit()
        print("USER=====", user)
        session['user_id'] = user.user_id

        return render_template("homepage.html")







@app.route('/recipes')
def recipes():
    """ recipes page"""

    recipes = Recipe.query.all()

    return render_template("recipes.html", recipes= recipes)


@app.route('/users/<user_id>')
def userpage(user_id):
    """ User favorites recipes"""

    user = User.query.filter_by(user_id=user_id).first()
    
    user_favorites_recipes = user.favorite_recipes

    return render_template("user.html", userfavorites = user_favorites_recipes)


@app.route('/add/recipe')
def addrecipe():
    """adding a recipe"""
    return render_template("newRecipeForm.html")


@app.route('/add/recipe')
def processaddrecipe():
    """processing adding a recipe"""

    name = request.form("recipename")
    instruction = request.form("instruction")
    preparationtime = request.form("preparationtime")
    dishtype= request.form("dishtype")
    recipeorigin = request.form("recipeorigin")


    recipe= Recipe(name=name, instruction=instruction, dishtype=dishtype, preparationtime=preparationtime, recipeorigin=recipeorigin)
    db.session.add(recipe)
    db.session.commit()



@app.route('/recipes/<recipe_id>')
def recipe(recipe_id):
    """ Displaying recipes based on ingredients"""

    recipe_id = recipe_id

    # payloads={"ingredients": ['apples','flour','sugar']}
    headers={
            "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
            "X-RapidAPI-Key": "0fd28a9296msh61f75fee9171434p1d6995jsn9f02884e2ae5"
        }
    # response = requests.get("https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/{id}/information",
    # headers=headers)
    response = requests.get(f"https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/{recipe_id}/information",
    headers={
    "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
    "X-RapidAPI-Key": "0fd28a9296msh61f75fee9171434p1d6995jsn9f02884e2ae5"
  }
)
    print(" \n\n\n\n\n\n\n\n RESPONSE IS =======>", response.json(), "\n\n\n\n\n\n")
    data = response.json()

    # id = data[0]["id"]

    title = data["title"]
    image = data["image"]
    likes = data.get("likes", 0)
    instruction = data.get("instructions", "none")

    print("instructions", instruction, "****************************")

    print("id", id)
    print("title", title)
    print("image", image)
    print("likes", likes)

     

    # response = requests.get(f"https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/{id}/analyzedInstructions?stepBreakdown=false",
    #     headers=headers
    #     )
    # data = response.json()
    # print("\n\n\n\n\n\n\n\n\n\n INSTRUCTION_data====>",data, "\n\n\n\n\n\n\n *************")
    # instruction = data[0]['steps'][0]['step']

    """ recipe videos"""
    payloads={"title": title}
    response = requests.get("https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/videos/search",
        params=payloads,
        headers=headers
        )

    data = response.json()
    print("\n\n\n\n", data, "\n\n\n")
    video = data.get('videos', "")
    print("videodata",data)


    return render_template("recipes.html",id=id, title=title, image=image, likes=likes, instruction=instruction, video=video, recipe_id= recipe_id)

    # user = User.query.filter_by(user_id=user_id).first()
    
    # user_favorites_recipes = user.favorite_recipes

    # return render_template("user.html", userfavorites = user_favorites_recipes)

@app.route('/recipes/<int:recipe_id>', methods=['POST'])
def likes(recipe_id):

    if session.get("user_id"):
        recipe_id = recipe_id
        user_id = session.get("user_id")
        userfavoriterecipe= UserFavoriteRecipe(user_id = user_id, recipe_id = recipe_id )
        db.session.add(userfavoriterecipe)
        db.session.commit()

        return redirect("/recipes/{recipe_id}")
    else:
        return redirect('/signin')


@app.route('/logout')
def logout():
    session[user_id]=None
    return redirect('/')







if __name__ == "__main__":

    app.jinja_env.auto_reload = app.debug

    connect_to_db(app)

    # Use the DebugToolbar
    # DebugToolbarExtension(app)

    app.run(debug=True)





