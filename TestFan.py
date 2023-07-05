# write a test program named TestFan that creates two Fan objects.

# pseudocode
# import the class from module created
from fan import Fan
# create the TestFan class
class TestFan:
   # implement the class contains
    def run_test(self):
        # establish the objects of two fans
        first_fan = Fan(Fan.FAST, True, 10, 'yellow')
        second_fan = Fan(Fan.MEDIUM, False, 5, 'blue')

    # recognize the command of first fan and print the output
    print("The First Fan has the following properties:")
    print("Speed:", first_fan.get_speed())
    print("Radius:", first_fan.get_radius())
    print("Color:", first_fan.get_color())
    print("Is the fan on?:", first_fan.is_on())
   
    # recognize the command of second fan and print the output

# run the program