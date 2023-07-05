# write a class named 'Car'  with the given data attributes
'''Methods: accelerate(), brake(), and get_speed().'''

# pseudocode
# create the class
class Car:
  # implement the constructor
  '''Use the __init__ method.'''
  def __init__(self, year_model, make):
      self.__year_model = year_model
      self.__make = make
      self.__speed = 0

  # establish the methods for car
  # set the car's speed in increase of 5
  def accelerate(self):
      self.__speed += 5

  # set the car's speed in decrease of 5
  def brake(self):
      self.__speed -= 5
      if self.__speed < 0:
          self.__speed = 0
          
  # method to get the current speed