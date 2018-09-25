# Week 4 Exercise 1
# Create a class, Triangle. It's __init__() constructor should take self
# angle1, angle2, and angle3 as paramters. Make sure to set the member
# variables appropriately in the body of the __init__() method.


class Triangle():
    """ This class describes a triangle """

    def __init__(self, angle1, angle2, angle3):
        self.__angle1 = angle1
        self.__angle2 = angle2
        self.__angle3 = angle3

    # All members of the class should be private. They should only be
    # accessible via Public Properties
    __angle1 = None
    __angle2 = None
    __angle3 = None

    def Angle1(self):
        return self.__angle1

    def Angle2(self):
        return self.__angle2

    def Angle3(self):
        return self.__angle3

    # Create a member variable in the Class named numberOfSides and set it
    # equal to 3
    __numberOfSides = 3

    def NumberOfSides(self):
        return self.__numberOfSides

    # Create a function named CheckAngles to calculate the sum of a triangle's
    # three angles. It should return True if the sum of the angles is 180 and
    # false if it is not

    def CheckAngles(self):
        if self.__angle1 + self.__angle2 + self.__angle3 == 180:
            return True
        else:
            return False

# Create a separate PY file in Visual studio where you will call the Class from
# -- Continued in Exercise1Main.py
