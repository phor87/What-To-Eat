import pickle

meal = pickle.load(open("meal.pickle", "rb"))

ingredient = open('ingredients.txt').read().splitlines()


def whatWeHave():
    """ prints a list of meal available if all ingredients is present """
    wehave = []
    for meals, ingredients in meal.items():
        if set(ingredients).issubset(ingredient):
            wehave.append(meals)
    print('We have', wehave)


def whatWeNeed(pick):
    """ prints what is needed from meal pick """
    weneed = []
    for items in meal[pick]:
        if items not in ingredient:
            weneed.append(items)
    print('For', pick, 'we need', weneed)


def addIngredient(stuff):
    """ add an ingredient to the list """
    if stuff == '':
        print('Nothing to add.')
    elif stuff not in ingredient:
        ingredient.append(stuff)
        print(stuff, 'added to ingredient.')
        thefile = open('ingredients.txt', 'w')
        for item in ingredient:
            thefile.write("%s\n" % item)
    elif stuff in ingredient:
        print(stuff, 'is already in ingredient.')


def removeIngredient(stuff):
    """ remove an ingredient from the list """
    if stuff in ingredient:
        ingredient.remove(stuff)
        print(stuff, 'was removed from ingredient.')
    elif stuff not in ingredient:
        print(stuff, 'is not in ingredient.')


def eat(stuff):
    """ check if stuff is available or prints a list of ingredients needed """
    if set(meal[stuff]).issubset(ingredient):
        print('We can eat', stuff)
    else:
        whatWeNeed(stuff)


def shoppingList():
    """ prints a shopping list of ingredients missing in all meals """
    shopping = []
    for meals, ingredients in meal.items():
        if not set(ingredients).issubset(ingredient):
            for items in ingredients:
                if items not in ingredient and items not in shopping:
                    shopping.append(items)
    print('Shopping list:', shopping)


def saveMeal():
    """ save meal dictionary """
    pickle_out = open("meal.pickle", "wb")
    pickle.dump(meal, pickle_out)
    pickle_out.close()
