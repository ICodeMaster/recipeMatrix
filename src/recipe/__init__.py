from component import ingredient as i


class RecipeIngredient():
        def __init__(self, amount, type, ingredient: i.Ingredient):
            self.amount = amount
            self.ingredient = ingredient
            self.measureType = type

class Recipe:

    def __init__(self, name, ingredients: list[RecipeIngredient] = []):
        self.name = name
        # TODO Alphabetize
        self.ingredients = ingredients
        self.steps = []
        self.yieldAmount = None
        # Total time, active time, passive time
        self.time = []
        # TODO Add tools
    def addRecipeIngredient(self, amount, type, ingredient: i.Ingredient):
        recipe_ingredient = RecipeIngredient(amount, type, ingredient)
        self.ingredients.append(recipe_ingredient)

    def defineStep(self, text, ingredients: list[i.Ingredient]):
        step = RecipeStep(text, ingredients)
        self.steps.append(step)

class RecipeStep:
    def __init__(self, text, ingredients: list[i.Ingredient]):
        # TODO Alphabetize
        self.text = text
        self.ingredients = ingredients