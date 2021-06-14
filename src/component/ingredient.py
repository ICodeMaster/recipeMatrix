from typing import *
from component import Component

class Ingredient(Component):
    def __init__(self, name):
        super().__init__(name)
        self.products = []
        self.density = None


class Product(Ingredient):

    def __init__(self, name, purchaseQuantity:dict[str, int]):
        super().__init__(name)
        self.purchaseDict = purchaseQuantity
        self.purchaseUnit = list(purchaseQuantity)[0]
        self.purchaseAmount = purchaseQuantity.get(self.purchaseUnit)

