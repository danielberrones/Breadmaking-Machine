import tkinter as tk
import random
import time

# List of bread types
bread_types = ["White Bread", "Whole Wheat Bread", "Sourdough Bread", "Rye Bread", "Multigrain Bread"]

# List of ingredients
ingredients = ["Flour", "Water", "Yeast", "Salt", "Sugar", "Butter", "Milk"]

# List of bake times in minutes
bake_times = [20, 25, 30, 35, 40]

# List of bake temperatures in Celsius
bake_temps = [180, 190, 200, 210, 220]

# List of seeds
seeds = ["Sesame seeds", "Poppy seeds", "Sunflower seeds", "Pumpkin seeds"]

# List of sweeteners
sweeteners = ["Honey", "Maple syrup", "Molasses", "Agave syrup"]

# Function to generate a random bread recipe
def generate_recipe():
    bread_type = random.choice(bread_types)
    ingredient1 = random.choice(ingredients)
    ingredient2 = random.choice(ingredients)
    ingredient3 = random.choice(ingredients)
    bake_time = random.choice(bake_times)
    bake_temp = random.choice(bake_temps)
    seed = random.choice(seeds)
    sweetener = random.choice(sweeteners)
    recipe = f"Bread Type: {bread_type}\nIngredients: {ingredient1}, {ingredient2}, {ingredient3}\nBake Time: {bake_time} minutes\nBake Temperature: {bake_temp}°C\nSeeds: {seed}\nSweetener: {sweetener}"
    recipe_text.delete('1.0', tk.END)  # Clear previous recipe
    recipe_text.insert(tk.END, recipe)

# Create main window
root = tk.Tk()
root.title("The Breadmaking Machine")

# Create splash screen label
splash_label = tk.Label(root, text="The Breadmaking Machine", font=("Helvetica", 24))
splash_label.pack(pady=20)

# Hide splash screen after 5 seconds
root.after(5000, splash_label.destroy)

# Create recipe display text widget
recipe_text = tk.Text(root, height=10, width=60)
recipe_text.pack()

# Create generate recipe button
generate_button = tk.Button(root, text="Generate Recipe", command=generate_recipe)
generate_button.pack()

# Run main loop
root.mainloop()

