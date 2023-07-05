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
  age = input("You're almost done! How old is your pet?: ")
  pet.set_age(age)

  # print the output
  print("Good Job! Here is the list of information of your lovely pet:")
  print("Name:", pet.get_name())
  print("Animal Type:", pet.get_animal_type())
  print("Age:", pet.get_age())

# check for errors
if __name__ == "__main__":
    main()
