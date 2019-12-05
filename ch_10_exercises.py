"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free
    Submit your completed file
"""
# import statement
import random


# The Dice class simulates a dice that can be tossed.

class Dice:

    # The __init__ method initializes the side up data attribute with sides 1-6.

    def __init__(self):
        self.__sideup = '1'  # Is it incorrect to do self.sideup + the number? yes

    # The toss method generates a random number in the range of 0 through 7. If the number is 0, then sideup is set
    # to '1'. If the number is 1, then sideup is set to '2', etc.

    def roll(self):
        if random.randint(0, 7) == 0:  # Is 7 the correct number to maximize the roll 1-6 since 0=1? yes
            self.__sideup = '1'
        elif random.randint(0, 7) == 1:
            self.__sideup = '2'
        elif random.randint(0, 7) == 2:
            self.__sideup = '3'
        elif random.randint(0, 7) == 3:
            self.__sideup = '4'
        elif random.randint(0, 7) == 4:
            self.__sideup = '5'
        else:

            self.__sideup = '6'

    def get_sideup(self):
        return self.__sideup


# The main function
def main():
    # Create an object from the Dice class
    my_dice = Dice()

    # Display the side of the dice that is facing up.
    print("This side is facing up:", my_dice.get_sideup())

    # Toss the dice
    print("I am going to toss the dice ten times: ")
    for count in range(10):
        my_dice.roll()

    # Display the side of the dice that is facing up.
    print("This side is facing up: ", my_dice.get_sideup())


# Call the main function
main()

"""


# TODO 10.2 modify Coin class to Dice
print("=" * 10, "Section 10.2 Coin class to Dice class", "=" * 10)

class Coin:  # note class names are capitalized
    def __init__(self):
        # TODO change side_up to '1'
        self.side_up = 'Heads'

        # TODO change toss() to roll()
    def toss(self):
        # TODO get a random value and set side_up for the 6 sides of the dice
        if random.randint(0, 1) == 0:
            self.side_up = 'Heads'
        else:
            self.side_up = 'Tails'
            
    def get_side_up(self):
        return self.side_up


# MY ATTEMPT
class Dice:  # note class names are capitalized
    def __init__(self):
        # TODO change side_up to '1'
        self.__sideup = '1'

        # TODO change toss() to roll()

    def roll(self):
        # TODO get a random value and set side_up for the 6 sides of the dice
        if random.randint(0, 1) == 0:
            self.__sideup = '1'
            self.__sideup = '2'
            self.__sideup = '3'
            self.__sideup = '4'
            self.__sideup = '5'

        else:
            self.__sideup = '6'

    def get_side_up(self):
        return self.__sideup


 
    # TODO change my_coin to my_dice, my_dice_two and the appropriate class name throughout main
    my_dice = Dice()
    my_dice_two = Dice()
    print('This side is up, ', my_dice.get_side_up())
    print('This side is up, ', my_dice_two.get_side_up())

    print('I am tossing the dice...')
    my_dice.toss()
    my_dice_two.toss()
    print('This side is up, ', my_dice.get_side_up())
    print('This side is up, ', my_dice_two.get_side_up())


main()
"""
