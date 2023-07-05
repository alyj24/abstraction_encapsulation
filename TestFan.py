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
        print("\033[97mThe First Fan has the following properties: ")
        print("\033[93mSpeed:" , first_fan.get_speed())
        print("\033[94mRadius:", first_fan.get_radius())
        print("\033[92mColor:", first_fan.get_color())
        print("\033[96mIs the fan on?:", first_fan.is_on())

        # recognize the command of second fan and print the output
        print("\033[97mThe Second Fan has the following properties: ")
        print("\033[91mSpeed:", second_fan.get_speed())
        print("\033[92mRadius:", second_fan.get_radius())
        print("\033[94mColor:", second_fan.get_color())
        print("\033[95mIs the fan on?:", second_fan.is_on())

# run the program
test = TestFan()
test.run_test()