# Running on a treadmill you burn 4.2 calories per minute. Write a program that uses a loop to display the number
# of calories burned after 10, 15, 20, 25 and 30 minutes

# Variables
for minutes in (10, 15, 20, 25, 30):
    calories_burned = minutes * 4.2
    print("You've burned", calories_burned,  "in", minutes, "minutes")
