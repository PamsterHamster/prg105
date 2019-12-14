# INSTRUCTIONS: Design a class that holds the following personal data: name, address, age and phone number.
# Write appropriate accessor and mutator methods(get & set).
# Write a program that creates three instances of the class. One instance should hold your information and the other
# two should hold your friends or family members' information. (Just add info, don't get it from the user.)
# Print the data from each object, make sure to format the output for clarity and ease of reading.


class PersonalData:

    #  the information needed from the data of classes
    def __init__(self, first, last, address, age, phone):
        self.first = first
        self.last = last
        self.address = address
        self.age = age
        self.phone = phone

    # the formatting for the data information
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def address(self):
        return '{}'.format(self.address)

    def age(self):
        return '{}'.format(self.age)

    def phone(self):
        return '{}'.format(self.phone)

    # the specific data used for the classes


me_data1 = PersonalData('Pam', 'Becker', 'any library', 'young at heart', 'XXX-1234')
friend_data2 = PersonalData('Teri', 'Tall', 'Heron Lane', '25 always', 'XXX-6578')
fam_data3 = PersonalData('Mom', 'Isgreat', 'Crystal Lake', 'getting up there', '123-XXXX')

#   Output
print(PersonalData.fullname(me_data1))
print(PersonalData.address(me_data1))
print(PersonalData.age(me_data1))
print(PersonalData.phone(me_data1))
print('--------------------------------')
print(PersonalData.fullname(friend_data2))
print(PersonalData.address(friend_data2))
print(PersonalData.age(friend_data2))
print(PersonalData.phone(friend_data2))
print('---------------------------------')
print(PersonalData.fullname(fam_data3))
print(PersonalData.address(fam_data3))
print(PersonalData.age(fam_data3))
print(PersonalData.phone(fam_data3))

"""
#   FIRST ATTEMPT

class PersonalData:
    def __init__(self, name, address, age, phone):
        self.name = name
        self.address = address
        self.age = age
        self.phone = phone

    def introduce_self(self):
        print("My name is " + self.name + "I live at" + self.address + "and I am " + self.age + "and call me at" +
              self.phone)

    # pdme = PersonalData()
    # pdme.name = "Pam"
    # pdme.address = "local library"
    # pdme.age = 25
    # pdme.phone = 8888888

    # pdfriend = PersonalData()
    # pdfriend.name = "Teri"
    # pdfriend.address = "Barharbor Drive"
    # pdfriend.age = 26
    # pdfriend.phone = 9999999

    pdme = PersonalData("Pam", "local library", 25, 8888888)
    pdfriend = PersonalData("Teri", "Barharbor Drive", 26, 9999999)

    #   Print the info

    pdme.introduce_self()
    pdfriend.introduce_self()

    
    # establish Class #1: My data     model page 540
    class MyData:
        def __init__(self, name, address, age, phone):
            self.__name = user
            self.__address = somewhere
            self.__age = youngatheart
            self.__phone = callme
    
        def set_name(self, name):
            self.__name = name
    
        def set_address(self, address):
            self.__address = address
    
        def set_age(self, age):
            self.__age = age
    
        def set_phone(self, phone):
            self.__phone = phone
    
        def get_name(self):
            return self.__name
    
        def get_address(self):
            return self.__address
    
        def get_age(self):
            return self.__age
    
        def get_phone(self):
            return self.__phone
    
    
    
    myself = MyData(name, address, age, phone)
    
    print('______________________________')
    print('Name: ', myself.get_name())
    print('Address: ', myself.get_address())
    print('Age: ', myself.get_age())
    print('Phone: ', myself.get_phone())
    
    
"""
# https://www.youtube.com/watch?v=uQUVEtnQ0LQ
