
chicken= Ingredient(ingredient_classification="Poultry",ingredient_name='chicken')
db.session.add(chicken)
db.session.commit()

tomato= Ingredient(ingredient_classification="veggies",ingredient_name='tomato')
db.session.add(tomato)
db.session.commit()

rice= Ingredient(ingredient_classification="grain",ingredient_name='rice')
db.session.add(rice)
db.session.commit()

cabbage= Ingredient(ingredient_classification="veggie",ingredient_name='cabbage')
db.session.add(cabbage)
db.session.commit()

garlic=Ingredient(ingredient_classification="spices",ingredient_name='garlic')
onions=Ingredient(ingredient_classification="veggie",ingredient_name='onions')
basil=Ingredient(ingredient_classification="spices",ingredient_name='basil')

friedrice= Recipe(instructions="fry rice with tomato, chicken and cabbage", dishtype='Main Dish', preparation_time=30, recipe_origin="Douala")
db.session.add(friedrice)
db.session.commit()

tomatosauce= Recipe(instructions="cooked puree tomatoes with garlic, basil and onions", dishtype="sauce", preparation_time=30, recipe_origin="Italia")
db.session.add(tomatosauce)
db.session.commit()

friedrice.ingredients_list.append(tomato)
friedrice.ingredients_list.append(chicken)
friedrice.ingredients_list.append(cabbage)


tomatosauce.ingredients_list.append(tomato)
tomatosauce.ingredients_list.append(garlic)
tomatosauce.ingredients_list.append(basil)
tomatosauce.ingredients_list.append(onions)





Michelle=User(fname='Michelle', lname='Ketcha', email='Michelle@gmail.com', password="lolo")
db.session.add(Michelle)
db.session.commit()

Ashley=User(fname='Ashley', lname='Ketcha', email='Asshley@gmail.com', password="lili")
db.session.add(Ashley)
db.commit()

Kara=User(fname='kara', lname='loi', email='kara@gmail.com', password="lele")
db.session.add(Kara)
db.session.commit()

christine=User(fname='christine', lname='lee', email='christine@gmail.com', password="aaa")
db.session.add(christine)
db.session.commit()

Samira=User(fname='Samira', lname='njayou', email='samira@gmail.com', password="bbb")
db.session.add(Samira)
db.session.commit()


Ashley.favorite_recipes(friedrice)










gingerbread= Recipe(instructions="bake flour with cinnnamon", dishtype='dessert', preparation_time=30, recipe_origin="USA")
gingerbread.ingredients_listgingerbread= Recipe(instruction="bake flour with cinnnamon", dishtype='dessert', preparation_time=30, recipe_origin="USA")
gingerbread.ingredients_list.append(cinnamon)
db.session.add(gingerbread)
db.session.commit()


all_ingredients[0]

all_ingredients[0].recipes[0]