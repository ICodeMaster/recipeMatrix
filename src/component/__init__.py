
class Component:
    __all__ = ["product", "recipeIngredient"]
    def __init__(self, name):
        self.name = name
        self.desc = None
        ### Portion size in grams
        self.portionSize = None
        ### Density in grams/mL
        self.Cost = None