print("Assignment 9".center(42, "="))
print("\033[94m=" * 48)
print("\033[95mCMPE-103-MODULE-06-ABSTRACTION-AND-ENCAPSULATION")
print("\033[94m=" * 48)

# design a class named "Fan" to represent a fan, then try and run the program.

# pseudocode
# create the class that will represent a fan
class Fan:
  # implement the fan speed
  '''Three constants that will set with values to denote the fan speed.'''
  SLOW = 1
  MEDIUM = 2
  FAST = 3
  # establish the constructor
  def __init__(self, speed=1, on=False, radius=1, color=blue):
      self.speed = speed
      self.on = on
      self.radius = radius
      self.color = color

  # construct the accessor and mutator methods for all four private data fields
  '''Accessor is also known as Getters while Mutator is Setters.'''
  # speed of the fan
  def get_speed(self):
      return self.speed

  def set_speed(self, speed):
      self.speed = speed

  # on-switch of the fan
  def is_on(self):
      return self.on

  def set_on(self, on):
      self.on = on

  # radius of the fan
  def get_radius(self):
      return self.radius

  def set_raduis(self, radius):
      self.radius = radius

  # color of the fan
  def get_color(self):
      return self.color

  def set_color(self, color):
      self.color = color