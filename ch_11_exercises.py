

"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free
    Submit your completed file
"""

# TODO 11.1 Introduction to Inheritance
print("=" * 10, "Section 11.1 inheritance", "=" * 10)


# You are going to create a Dwelling class based on the
# Automobile sample from the chapter

# 1) Create the class Dwelling, the __init__ method should accept number_of_rooms, square_feet, floors
class Dwelling:

    def __init__(self, number_of_rooms, square_feet, floors):
        self.__number_of_rooms = number_of_rooms  # Can I name it this? YES must be the same to initialize
        self.__square_feet = square_feet
        self.__floors = floors

    # 2) Add mutators for all of the data attributes (number_of_rooms, square_feet, floors)
    def set_number_of_rooms(self, number_of_rooms):
        self.__number_of_rooms = number_of_rooms

    def set_square_feet(self, square_feet):
        self.__square_feet = square_feet

    def set_floors(self, floors):
        self.__floors = floors

    # 3) Add accessors for all of the data attributes
    def get_number_of_rooms(self):
        return self.__number_of_rooms

    def get_square_feet(self):
        return self.__square_feet

    def get_floors(self):
        return self.__floors


# 4) Create the class SingleFamilyHome as a sub class of Dwelling  Book page 555 example

class SingleFamilyHouse(Dwelling):

    # The __init__ method should accept number_of_rooms, square_feet, floors, garage_type, yard_size

    def __init__(self, number_of_rooms, square_feet, floors, garage_type, yard_size):
        # -- Call the __init__ of superclass Dwelling and pass the required arguments, remember to include self
        Dwelling.__init__(self, number_of_rooms, square_feet, floors)

        # -- Initialize the garage_type and yard_size attributes
        self.__garage_type = garage_type
        self.__yard_size = yard_size

    # 5) Create the mutator and accessor methods for the garage_type and yard_size attributes
    # Mutators
    def set_garage_type(self, garage_type):
        self.__garage_type = garage_type

    def set_yard_size(self, yard_size):
        self.__yard_size = yard_size

    # Accessors
    def get_garagetype(self):
        return self.__garage_type

    def get_yardsize(self):
        return self.__yard_size

    # Demonstrate the SingleFamilyHome class, no need to import because you are in the same file  FINISH THIS SECTION!
    # 6) Create a main function.


def main():
    # 7) In main, create an object from the Single_family_home class with the following information:
    #  6 rooms, 1200 square feet, 1 floor, single car garage, .25 acres
    avail_for_sale = SingleFamilyHouse.Dwelling('6', 1200, 1, 'single', .25)
    # WHY DOESN"T LINE ABOVE WORK? Isn't the formula:    new variable name = subclass.Class(detailed attributes)

    # # 8) Display the data using the accessor methods

    print('Dwellings available')
    print('===================================')
    print('The following Dwellings are in the inventory for sale: ')
    print('Number of rooms: ', avail_for_sale.get_number_of_rooms())
    print('Square Feet: ', avail_for_sale.get_square_feet())
    print('Number of floors: ', avail_for_sale.get_floors())
    print('Yard size: ', avail_for_sale.get_yard_size())

    # # 9) Call the main function


main()

"""
    # TODO 11.2 Polymorphism
    print("=" * 10, "Section 11.2 polymorphism", "=" * 10)

    # 1) Type in the mammal class from program 11-9, lines 1 - 22  Page 566


class Mammal:

    # The __init__ method accepts an argument for the mammal's species.

    def __init__(self, species):
        self.__species = species

    # The show_species method displays a message indicating the mammal's species

    def show_species(self):
        print('I am a', self.__species)

    # The make_sound method is the mammal's way of making a generic sound.
    def make_sound(self):
        print('Grrrrr')


# 2) Create a Mouse class as a sub class of the mammal class following the Dog example
class Mouse(Mammal):

    # The __init__ method calls the superclass's, __init__ method passing "Mouse" as the species.

    def __init__(self):
        Mammal.__init__(self, 'Mouse')

        # The make_sound method overrides the superclass's make_sound method.

    def make_sound(self):
        print('squeak squeak ')


# 3) Create an Sheep class as a sub class of the mammal class following the Cat Example

class Sheep(Mammal):
    #  The __init__ method calls the superclass's
    # __init__ method passing 'Sheep' as the species.

    def __init__(self):
        Mammal.__init__(self, 'Sheep')

    # The make_sound method overrides the superclass's make_sound method.

    def make_sound(self):
        print('Baaaaa')


# 4) Follow the example in program 11-10 (no need to import, use main2 instead of main
#    because there is already a main on this page) use the Mouse and Sheep class that you created

def main2():
    # Create a Mammal object, a Mouse object, and a Sheep object
    mammal = Mammal('regular animal')
    mouse = Mouse()
    sheep = Sheep()

    # Display information about each one.
    print('Here are some animals and the sound they make.')
    print('---------------------------------------')
    show_mammal_info(mammal)
    print()
    show_mammal_info(mouse)
    print()
    show_mammal_info(sheep)
    print()  # Isn's this print statement needed? Not in example 11-10 page 569


# The show_mammal_info function accepts an object as an argument, and calls its show_species and make_sound methods.

def show_mammal_info(creature):
    creature.show_species()
    creature.make_sound()


mammal = Mammal('regular mammal')
mammal.show_species()
mammal.make_sound()

# Call the main2 function
main2()
"""
