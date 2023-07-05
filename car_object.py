# design a program that creates a Car object then calls the accelerate method five times.
# after each call to the accelerate method, get the current speed of the car and display it.
# then, call the brake method for five times.
# after each call to the brake method, get the current speed of the car and display it.

# pseudocode
# import class from the module created
from car import Car
# implement functions
def main():
    # establish the object of the car
    car = Car(2005, "Chevrolet Equinox")

    # call the program to accelerate, five times
    for _ in range(5):
        car.accelerate()
        # print the output
        print("\033[91mAfter the acceleration of the car~")
        print("\033[94mThe current speed of Chevrolet Equinox is ", car.get_speed())

    # call the program to brake, five times
    for _ in range(5):
        car.brake()
        # print the output
        print("\033[91mAfter the brake of the car~")
        print("\033[93mThe current speed of Chevrolet Equinox is ", car.get_speed())

# check for errors
if __name__ == "__main__":
    main()

