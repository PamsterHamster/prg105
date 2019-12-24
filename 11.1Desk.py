class Desk(OfficeFurniture):
    # initialize
    def __init__(self, material, size, price, drawerlocation, number, color):
        # Call the superclass's __init__ method and pass the required arguments, incl 'self'
        OfficeFurniture.__init__(self, material, size, price)

        # initialize the __drawerlocation, number & color
        self.__drawerlocation = drawerlocation
        self.__number = number
        self.__color = color

        # Set the mutators for the drawerlocation, number & color

    def set_drawerlocation(self, drawerlocation):
        self.__drawerlocation = drawerlocation

    def set_number(self, number):
        self.__number = number

    def set_color(self, color):
        self.__color = color

        # Set accessors for the drawerlocation, number, & color

    def get_drawerlocation(self):
        return self.__drawerlocation

    def get_number(self):
        return self.__number

    def get_color(self):
        return self.__color

    def __str__(self):
        return '\nMaterial: ' + self.get__material() + \
               '\nSize: ' + self.get__size() + \
               '\nPrice: ' + self.get__price() + \
               '\nDrawer Location: ' + self.__drawerlocation + '\nNumber of Drawers: ' + self.__number + \
               '\nColor: ' + self.__color


my_desk = Desk.OfficeFurniture('Vinyl', 'student', '$100.00', 'right drawers', '2 drawers', 'dark cherry')
print(my_desk)
