import pickle
import discord

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
            return 'We have nothing.'
        else:

            return 'We have ' + ', '.join(a_list)
    else:
        for item in recipes_dict:
            if ingredient in recipes_dict[item]:
                a_list.append(item)
        if not a_list:
            return 'Nothing has ' + str(ingredient) + ' in it.'
        else:
            return 'These have ' + str(ingredient) + ' in it: ' + ', '.join(a_list)


def add(ingredient):
    """ add an ingredient to the list """
    ingredient = ingredient.lower()
    if ingredient == '':
        return 'Nothing to add.'
    elif ingredient not in ingredients_list:
        ingredients_list.append(ingredient)
        return str(ingredient) + ' added to ingredients list.'
        update_list()
    elif ingredient in ingredients_list:
        return str(ingredient) + ' is already on the list.'


def remove(ingredient):
    """ remove an ingredient from the list """
    if ingredient == '':
        return 'Nothing to add.'
    if ingredient in ingredients_list:
        ingredients_list.remove(ingredient)
        return str(ingredient) + ' was removed from the list.'
        update_list()
    elif ingredient not in ingredients_list:
        return str(ingredient) + ' is not in the list.'


def eat(something):
    """ check if something is available or prints a list of ingredients needed """
    if set(recipes_dict[something]).issubset(ingredients_list):
        return 'We can eat ' + str(something)
    else:  # prints what ingredients are needed
        a_list = []
        for ingredient in recipes_dict[something]:
            if ingredient not in ingredients_list:
                a_list.append(ingredient)
        return 'For ' + str(something) + ', we need' + ', '.join(a_list)


def shop():
    """ prints a shopping list of ingredients missing in all meals """
    shopping_list = []
    for recipe, ingredient in recipes_dict.items():
        if not set(ingredient).issubset(ingredients_list):
            for items in ingredient:
                if items not in ingredients_list and items not in shopping_list:
                    shopping_list.append(items)
    return 'Shopping list: ' + ', '.join(shopping_list)


def save():
    """ save recipes dictionary """
    pickle_out = open("recipes.pickle", "wb")
    pickle.dump(recipes_dict, pickle_out)
    pickle_out.close()


def list_recipes():
    """ list recipes from dictionary """
    return ', '.join(str(recipe) for recipe in recipes_dict)


def list_ingredients():
    """ list ingredients from list """
    return ', '.join(str(items) for items in ingredients_list)

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('.have'):
        await client.send_message(message.channel, have())

    if message.content.startswith('.recipes'):
        await client.send_message(message.channel, list_recipes())

    if message.content.startswith('.ingredients'):
        await client.send_message(message.channel, list_ingredients())

    if message.content.startswith('.shop'):
        await client.send_message(message.channel, shop())

    if message.content.startswith('.add'):
        item = await client.wait_for_message(timeout=20.0, author=message.author)
        await client.send_message(message.channel, add(str(item.content)))

    if message.content.startswith('.remove'):
        item = await client.wait_for_message(timeout=20.0, author=message.author)
        await client.send_message(message.channel, remove(str(item.content)))

    if message.content.startswith('.eat'):
        item = await client.wait_for_message(timeout=20.0, author=message.author)
        await client.send_message(message.channel, eat(str(item.content)))

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('token')