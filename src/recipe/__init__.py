from component import ingredient as i

class Recipe:

    def __init__(self, name, ingredients: list[i.Ingredient:dict[str, int]]):
        self.name = name
        # TODO Alphabetize
        self.ingredients = ingredients
        self.steps = []
        self.yieldAmount = None
        # Total time, active time, passive time
        self.time = []
        # TODO Add tools


    def defineStep(self, text, ingredients: list[i.Ingredient]):
        step = RecipeStep(text, ingredients)
        self.steps.append(step)

class RecipeStep:
    def __init__(self, text, ingredients: list[i.Ingredient]):
        # TODO Alphabetize
        self.text = text
        self.ingredients = ingredients