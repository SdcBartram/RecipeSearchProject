# JenSam Recipe Finder Programme
import requests
from pprint import pprint

# welcome message
print('\nWelcome to JenSam Recipe Finder, banishing those "What Shall We Have For Dinner?" blues since 2022')


# Recipe Search Function
def recipe_search(ingredient, exclusions, meal_type):
    # Register to get an APP ID and key https://developer.edamam.com/
    app_id = ''
    app_key = ''
    parameters = {
        'mealType': meal_type
    }
    result = requests.get(
        'https://api.edamam.com/search?q={}&app_id={}&app_key={}&excluded={}'.format(ingredient, app_id, app_key,
                                                                                     exclusions), params=parameters)

    # Return the list of different recipes
    recipe_list = result.json()['hits']

    return recipe_list


def user_input():
    # Prompt user for main ingredient
    ingredient = input('\nWhat is your main ingredient? ')
    # Prompt user for excluded ingredients
    exclusions = input('\nWhat ingredients need to be excluded? ')
    # Prompt user for meal type
    meal_type = input('\nWhat meal are you cooking, for example breakfast, lunch or dinner? ')
    # Get results from API
    recipe_list = recipe_search(ingredient, exclusions, meal_type)

    # Create an index variable to keep track of the items
    index = 0

    for recipe in recipe_list:
        recipe_name = recipe['recipe']['label']
        print()
        print(index, recipe_name)
        index += 1

    # User can select a recipe and convert it to an integer, so list can be filtered at a later stage
    while True:
        try:
            selected_recipe_number = int(input('\nWhat number meal would you like? '))
            break
        except ValueError:
            print('\nSorry that is not a number. ')

    # If the selected number is in the list, return the label, uri and ingredients

    # First check to see if the number is a valid one
    if selected_recipe_number <= (len(recipe_list) - 1):
        # Filter the full results to the selected recipe
        selected_recipe = recipe_list[selected_recipe_number]
        # Print the relevant results
        print(selected_recipe['recipe']['label'])
        print(selected_recipe['recipe']['url'])
        pprint(selected_recipe['recipe']['ingredientLines'])
        print()

        # Prompt the user to save recipe
        r = input('Would you like to save your recipe? Y or N ').upper()
        if r == 'Y':
            with open('my_recipe.txt', 'w+') as text_file:
                label = (selected_recipe['recipe']['label'])
                website = (selected_recipe['recipe']['url'])
                text_file.write(label + '\n' + website)
        else:
            print('\nYou have selected not to save the recipe')


user_input()
