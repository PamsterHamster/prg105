# TODO:
# A nutritionist who works for a fitness club helps members by evaluating their diets.
# As part of her evaluation, she asks members for the number of grams each in fat, carbs, and protein consumed in a day.
# Then she calculation the number of calories each from fat, carbs, and protein using the following formula:
# calories from fat = fat grams x 9
# calories from carbs = carb grams x 4
# calories from protein = protein grams x 4


# Use a different function for each nutrient to make calculations by nutrient,
# and print the calories for that nutrient on screen.
# Return the results from each function to variables in the main method.
# Add the variables in the main method to display the total calories for the day.

# Functions--My attempt
def calculate_caloriesfrom_fat(fat_grams):
    caloriesfrom_fat = fat_grams * 9
    return caloriesfrom_fat


def calculate_caloriesfrom_carbs(carb_grams):
    caloriesfrom_carbs = carb_grams * 4
    return caloriesfrom_carbs


def calculate_caloriesfrom_protein(protein_grams):
    caloriesfrom_protein = protein_grams * 4
    return caloriesfrom_protein


def main():
    user_fatgrams = float(input("Enter fat grams: "))
    user_carbgrams = float(input("Enter carb grams: "))
    user_proteingrams = float(input("Enter protein grams: "))

    calories_from_fat = calculatecaloriesfrom_fat(user_fatgrams)
    calories_from_carbs = calculatecaloriesfrom_carbs(user_carbgrams)
    calories_from_protein = calculatecaloriesfrom_protein(user_proteingrams)

    print("Calories from Fat: ", format(calories_from_fat, ".2f"))
    print("Calories from Carbs: ", format(calories_from_carbs, ".2f"))
    print("Calories from Protein: ", format(caloriesfrom_protein, ".2f"))


"""
# Variables
fat = float(input(grams_day))
carbs = float(input(grams_day))
protein = float(input(grams_day))

grams_day = nutrient
nutrient1 = fat
nutrient2 = carbs
nutrient3 = protein

# Calculations: FatCalFrom_nutrient = int(input(nutrient * form_num))

FatCalFrom_nutrient1 = float(input(nutrient1 * 9))
FatCalFrom_nutrient2 = float(input(nutrient2 * 4))
FatCalFrom_nutrient3 = float(input(nutrient3 * 4))

# Input
# ask How many grams of fat do you eat in one day?
float(input("How many grams of fat do you eat in one day? : "))

# ask How many grams of carbs do you eat in one day?
float(input("How many grams of carbs do you eat in one day? : "))

# ask How many grams of protein do you eat in one day?
float(input("How many grams of protein do you eat in one day? : "))

# Storage of Total Grams from calculations--convert str to floats


# Display output via print statements


main()
"""
