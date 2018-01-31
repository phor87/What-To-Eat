import pickle

recipes_dict = pickle.load(open("recipes.pickle", "rb"))
ingredients_list = open('ingredients.txt').read().splitlines()


def update_list():
    """ update ingredients list """
    the_file = open('ingredients.txt', 'w')
    for item in ingredients_list:
        the_file.write("%s\n" % item)


def have(ingredient=None):
    """ prints a list of recipes available if all ingredients is present.
        or prints what recipes has an ingredient."""
    a_list = []
    if ingredient is None:
        for recipe, ingredient in recipes_dict.items():
            if set(ingredient).issubset(ingredients_list):
                a_list.append(recipe)
        if not a_list:
            print('We have nothing.')
        else:
            print('We have', a_list)
    else:
        for item in recipes_dict:
            if ingredient in recipes_dict[item]:
                a_list.append(item)
        if not a_list:
            print('Nothing has', ingredient, 'in it.')
        else:
            print('These have', ingredient, 'in it.', a_list)


def add(ingredient):
    """ add an ingredient to the list """
    ingredient = ingredient.lower()
    if ingredient == '':
        print('Nothing to add.')
    elif ingredient not in ingredients_list:
        ingredients_list.append(ingredient)
        print(ingredient, 'added to ingredients list.')
        update_list()
    elif ingredient in ingredients_list:
        print(ingredient, 'is already in ingredients list.')


def remove(ingredient):
    """ remove an ingredient from the list """
    if ingredient == '':
        print('Nothing to add.')
    if ingredient in ingredients_list:
        ingredients_list.remove(ingredient)
        print(ingredient, 'was removed from ingredients list.')
        update_list()
    elif ingredient not in ingredients_list:
        print(ingredient, 'is not in the ingredients list.')


def eat(something):
    """ check if something is available or prints a list of ingredients needed """
    if set(recipes_dict[something]).issubset(ingredients_list):
        print('We can eat', something)
    else:  # prints what ingredients are needed
        a_list = []
        for ingredient in recipes_dict[something]:
            if ingredient not in ingredients_list:
                a_list.append(ingredient)
        print('For', something, 'we need', a_list)


def shop():
    """ prints a shopping list of ingredients missing in all meals """
    shopping_list = []
    for recipe, ingredient in recipes_dict.items():
        if not set(ingredient).issubset(ingredients_list):
            for items in ingredient:
                if items not in ingredients_list and items not in shopping_list:
                    shopping_list.append(items)
    print('Shopping list:', shopping_list)


def save():
    """ save recipes dictionary """
    pickle_out = open("recipes.pickle", "wb")
    pickle.dump(recipes_dict, pickle_out)
    pickle_out.close()


def list_recipes():
    """ list recipes from dictionary """
    for recipe in recipes_dict:
        print(recipe)


def list_ingredients():
    """ list ingredients from list """
    for items in ingredients_list:
        print(items)
