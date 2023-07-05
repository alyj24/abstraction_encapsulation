# write a program that creates an object of the class,
# prompts the user to enter the name, type, and age of his or her pet,
# store the data, use object's acccessor and display.

# pseudocode
# import the class from module created
from pet import Pet
# implement functions
def main():
    pet = Pet()
  # ask the user for an inputs and save it all
  # name of the pet
    name = input("\033[93mGreat Day! Please enter the name of your pet: ")
    pet.set_name(name)

  # animal type of the pet
    animal_type = input("\033[96mNow, enter the animal type of your pet: ")
    pet.set_animal_type(animal_type)

  # age of the pet
    age = input("\033[97mYou're almost done! How old is your pet?: ")
    pet.set_age(age)

  # print the output
    print("\033[95mGood Job! Here is the list of information of your lovely pet:")
    print("\033[91mName:", pet.get_name())
    print("\033[92mAnimal Type:", pet.get_animal_type())
    print("\033[94mAge:", pet.get_age())

# check for errors
if __name__ == "__main__":
    main()
