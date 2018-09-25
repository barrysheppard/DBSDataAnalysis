# Example of a class
class Customer(object):
    """ This describes a customer """
    ###########################
    # Member Variables        #
    ###########################

    # The two underscores at the start make these private variables
    # This means objectName.firstName will no longer work.
    __firstName = None
    __lastName = None
    __age = None

    ###########################
    # Properties              #
    ###########################

    def setFirstName(self, value):
        # Logic to make sure the name is valid
        self.__firstName = value

    def setAge(self, value):
        if(value < 18):
            raise Exception("Must be over 18")
        else:
            self.__age = value

    ###########################
    # Class Functions         #
    ###########################

    def PrintCustomer(self):
        print("First Name:", self.__firstName)
        print("Last Name:", self.__lastName)
        print("Age:", self.__age)

    def getFirstName(self):
        return self.__firstName

    def getAge(self):
        return self.__Age

    ###########################
    # Constructor             #
    ###########################
    def __init__(self, fName, lName):
        self.__firstName = fName
        self.__lastName = lName
