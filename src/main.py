#%%
import sys
import tkinter as tk
from tkinter.constants import E, END, LEFT, RIGHT, TOP, W
sys.path.append('C:/Users/user/Documents/Recipe Do-Dad/recipeMatrix/src')
from component import (ingredient as ig)
import recipe as r
import recipe_utils

def updateRecipeName(entry, recipeName: r.Recipe):
    recipeName.name = entry.get()
porkIngrd = ig.Ingredient("Pork Shoulder")
yougurtIngrd = ig.Ingredient("Yogurt")
cukeIngrd = ig.Ingredient("Cucumber")
masterRecipe = r.Recipe("Tandaloo")
masterRecipe.addRecipeIngredient(3, "lb", porkIngrd)
masterRecipe.addRecipeIngredient(6, "cup", yougurtIngrd)
masterRecipe.addRecipeIngredient(500, "g", cukeIngrd)
subRecipe = r.Recipe("Saucy-Sauce")
subRecipe.addRecipeIngredient(6, "g", yougurtIngrd)
subRecipe.addRecipeIngredient(40, "oz", cukeIngrd)
masterRecipe.addRecipeIngredient(40, "oz", subRecipe)
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.currentIngredients = []
        self.frames = []
        self.pack()
        self.create_widgets()
        self.loadRecipe(masterRecipe)
    class FrameEntry(tk.Frame):
        def __init__(self, recipeComponent: r.RecipeComponent, master=None):
            super().__init__(master)
            #self.pack()
            self.master = master
            self.recipeComponent = recipeComponent
            self.frames = []
            self.entry_name = tk.Label(self)
            self.entry_name["text"] = str(recipeComponent.ingredient.name) + ":" + str(recipeComponent.amount) + str(recipeComponent.measureType)
            self.button_remove = tk.Button(self, text="Remove")
            self.button_remove["command"] = self.removeButtonClick
            self.entry_name.grid(row = 0, column=0, columnspan=2, sticky="w",padx=15,pady=5)
            self.button_remove.grid(row=0, column=2, sticky="e",padx=15,pady=5)
            if recipeComponent.isRecipe():
                self.createSubRecipeFrames(recipeComponent.ingredient)
                self.currentRecipe = self.recipeComponent.ingredient
        def removeButtonClick(self):
            try:
                ### Find yourself in master array
                i_remove = self.master.frames.index(self)
                ### Remove corresponding data entry
                self.master.currentRecipe.componentList.pop(i_remove)
                self.master.frames.remove(self)
                self.destroy()
            except:
                print("fail remove" + str(self))
        def createSubRecipeFrames(self, recipe):
            for i, currentIngredient in enumerate(recipe.componentList, start=1):
                frame_entry = self.__class__(currentIngredient, master=self)
                frame_entry.grid(column=1, row=1+i, columnspan=2, sticky="e",padx=15,pady=5)
                frame_entry["bg"] = "red"
                self.frames.append(frame_entry)


    def loadRecipe(self, recipe: r.Recipe):
        self.recipeNameEntry["text"] = recipe.name
        self.currentRecipe = recipe
        self.populateIngredients(recipe)
    def create_widgets(self):
        self.recipeNameEntry = tk.Label(self)
        self.recipeNameEntry.grid(row = 1, column=0 )
        #self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.grid(row = 1, column = 1)
    def populateIngredients(self, recipe: r.Recipe):
        for i in self.frames:
            self.frames[i].destroy()
        self.frames.clear()
        for i, currentIngredient in enumerate(recipe.componentList, start=1):
            frame_entry = self.FrameEntry(currentIngredient, master=self)
            frame_entry.grid(sticky="ew",row = i+2, column=0, padx=0, pady=5)
            frame_entry["bg"] = "blue"
            self.frames.append(frame_entry)

root = tk.Tk()
app = Application(master=root)
app.mainloop()
# %%

