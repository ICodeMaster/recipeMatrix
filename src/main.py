#%%
import sys
import tkinter as tk
sys.path.append('C:/Users/user/Documents/Recipe Do-Dad/recipeMatrix/src')
from component import (ingredient as i)
import recipe as r
import recipe_utils

def updateRecipeName(entry, recipeName: r.Recipe):
    recipeName.name = entry.get()

window = tk.Tk()

label = tk.Label(text = "Recipe")
label.pack()
recipeName = tk.StringVar()
recipeNameEntry = tk.Entry(textvariable=recipeName)
blankRecipe = r.Recipe(recipeName, None)
recipeName.trace_add("write", updateRecipeName(args, recipeNameEntry, blankRecipe))
recipeNameEntry.pack()
window.mainloop()
# %%
