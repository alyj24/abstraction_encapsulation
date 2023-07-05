# write a class named 'Pet' with the given data attributes
'''Methods: set_name(), set_animal_type(), set_age(), get_name(), get_animal_type(), and get_age()'''

# pseudocode
# create the class
class Pet:
    # implement the constructor
    '''Use the __init__ method.'''
    def __init__(self):
        self.__name = ""
        self.__animal_type = ""
        self.__age = 0

    # establish the methods for the pet
    # assigns a value to the name field
    def set_name(self, name):
        self.__name = name

    # assigns a value to the animal type field
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    # assigns a value to the age field
    def set_age(self, age):
        self.__age = age
        
    # return the value of the name field
    # return the value of the animal type field
    # return the value of the age field