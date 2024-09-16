"""
Implementation of: LU02.A08 - Kochbuch
"""

import json


def load_recipe(json_string):
    return json.loads(json_string)


def adjust_recipe(recipe, new_servings):
    factor = new_servings / recipe['servings']
    adjusted_ingredients = {ingredient: amount * factor for ingredient, amount in recipe['ingredients'].items()}

    return {'title': recipe['title'], 'ingredients': adjusted_ingredients, 'servings': new_servings}


if __name__ == '__main__':
    # Beispiel für die Datenstruktur eines Rezepts
    recipe_json = '{"title": "Spaghetti Bolognese", "ingredients": {"Spaghetti": 400, "Tomato Sauce": 300, "Minced Meat": 500}, "servings": 4}'

    # Rezept aus JSON laden
    recipe_object = load_recipe(recipe_json)

    # Neue Anzahl von Personen
    new_servings_amount = 2

    # Angepasstes Rezept berechnen
    adjusted_recipe = adjust_recipe(recipe_object, new_servings_amount)

    # Ausgabe des angepassten Rezepts
    print(json.dumps(adjusted_recipe, indent=4))
