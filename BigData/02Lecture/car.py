# In this example we will create a variable called Car.


class Car(object):
    ''' This class represents a Car '''

    def __init__(self):
        self.__colour = ''
        self.__make = ''
        self.__model = ''
        self.__mileage = 0
        self.engineSize = ''

    def setColour(self, colour):
        self.__colour = colour

    def getColour(self):
        return self.__colour

    def setMake(self, make):
        self.__make = make

    def getMake(self):
        return self.__make

    def setModel(self, model):
        self.__make = model

    def getModel(self):
        return self.__model

    def setMileage(self, mileage):
        self.__mileage = mileage

    def getMileage(self):
        return self.__mileage

    # To model behaviour we have methods

    def move(self, distance):
        print("Moved", str(distance), "kms")
        self.__mileage += distance


RedFerrari = Car()
# If we print this object it will tell us what time of object it is and
# where in memory it is stored
print(RedFerrari)

# For the public variable we can directly assign a new value to it
RedFerrari.engineSize = '3.5'
print(RedFerrari.engineSize)

# For the private variables we have to use the setters to change them
RedFerrari.setColour('Red')
# and we have to  use the getters to access them
print(RedFerrari.getColour())

RedFerrari.setMake('Ferrari')
print(RedFerrari.getMake())

RedFerrari.setMileage(26)
print(RedFerrari.getMileage())

# We can make another instance, a diferent object

yellowTaxi = Car()
yellowTaxi.setMake('Toyota')
yellowTaxi.setColour('Yellow')
yellowTaxi.setMileage(120004)
print(yellowTaxi.getMake())
print(yellowTaxi.getColour())
print(yellowTaxi.getMileage())

yellowTaxi.move(5)
print(yellowTaxi.getMileage())
