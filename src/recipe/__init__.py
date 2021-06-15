from component import ingredient as i


class RecipeComponent():
        def __init__(self, amount, type, ingredient):
            self.amount = amount
            self.ingredient = ingredient
            self.measureType = type
        def isIngredient(self):
            if isinstance(self.ingredient, i.Ingredient):
                return True
            else:
                return False
        def isRecipe(self):
            if isinstance(self.ingredient, Recipe):
                return True
            else:
                return False


class Recipe:

    def __init__(self, name):
        self.name = name
        # TODO Alphabetize
        self.componentList = []
        self.steps = []
        self.yieldAmount = None
        # Total time, active time, passive time
        self.time = []
        # TODO Add tools
    def addRecipeIngredient(self, amount, type, ingredient: i.Ingredient):
        recipe_ingredient = RecipeComponent(amount, type, ingredient)
        self.componentList.append(recipe_ingredient)

    def defineStep(self, text, ingredients: list[i.Ingredient]):
        step = RecipeStep(text, ingredients)
        self.steps.append(step)

class RecipeStep:
    def __init__(self, text, ingredients: list[i.Ingredient]):
        # TODO Alphabetize
        self.text = text
        self.ingredients = ingredients