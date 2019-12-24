class OfficeFurniture:
    # initialize
    def __init__(self, material, size, price):
        self.__material = material
        self.__size = size
        self.__price = price

        # Mutators

    def set_material(self, material):
        self.__material = material

    def set_size(self, size):
        self.__size = size

    def set_price(self, price):
        self.__price = price

        # Accessors

    def get_material(self):
        return self.__material

    def get_size(self):
        return self.__size

    def get_price(self):
        return self.__price

    def __str__(self):
        return '\nMaterial: ' + self.__material + '\nSize: ' + self.__size + '\nPrice: ' + self.__price


my_recliner = OfficeFurniture('cloth', 'adult sleeper', '$1500.00')
print(my_recliner)
