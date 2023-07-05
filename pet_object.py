# write a program that creates an object of the class,
# prompts the user to enter the name, type, and age of his or her pet,
# store the data, use object's acccessor and display.

# pseudocode
# import the class from module created
from pet import Pet
# implement functions
def main()
    pet = Pet()
  # ask the user for an inputs and save it all
  # name of the pet
  name = input("Great Day! Please enter the name of your pet: ")
  pet.set_name(name)

  # animal type of the pet
  animal_type = input("Now, enter the animal type of your pet: ")
  pet.set_animal_type(animal_type)
  
  # age of the pet
  # print the output
# check for errors
