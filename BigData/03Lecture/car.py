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


# In this example we are extending the base class of Car
class ElectricCar(Car):

    def __init__(self):
        # Here were are calling the __init__ from the Car class
        # This private __ method from Car that we can call
        Car.__init__(self)
        # For electric cards we also have an extra variable to set
        self.__numberFuelCells = 1

    def getNumberFuelCells(self):
        return self.__numberFuelCells

    def setNumberFuelCells(self, numberFuelCells):
        self.__numberFuelCells = numberFuelCells


electric = ElectricCar()
electric.setMake("Nissan")
electric.setModel("Leaf")
print(electric.getNumberFuelCells())
print(electric.getMake())
print(electric.getModel())


# We can also use this to make other types of car
class PetrolCar(Car):

    def __init__(self):
        Car.__init__(self)
        self.__engineSize = 1

    def getEngineSize(self):
        return self.__engineSize

    def setEngineSize(self, engineSize):
        self.__engineSize = engineSize


class CarFleet(object):

    def __init__(self):
        self.__petrol_cars = []
        self.__electric_cars = []
        # This creates 10 petrol car objects and 5 electric cars
        for i in range(1, 11):
            self.__petrol_cars.append(PetrolCar())
        for i in range(1, 6):
            self.__electric_cars.append(ElectricCar())

    def getPetrolCars(self):
        return self.__petrol_cars

    def getElectricCars(self):
        return self.__electric_cars

    def checkCarsInStock(self):
        '''This prints the number of petrol and electric cars'''
        print('Petrol Cars : ' + str(len(self.getPetrolCars())))
        print('Electric Cars : ' + str(len(self.getElectricCars())))

    def rent(self, cartype):
        ''' This removes a car of the specified type '''
        if cartype == 'P':
            self.__petrol_cars.pop()
        elif cartype == 'E':
            self.__electric_cars.pop()

    def returnCar(self, cartype, rentedCar):
        ''' This removes a car of the specified type '''
        if cartype == 'P':
            self.__petrol_cars.append(rentedCar)
        elif cartype == 'E':
            self.__electric_cars.append(rentedCar)

    def mainMenu(self):
        print('Welcome to Europcar')
        rentedCar = None
        msg = 'Would you like to rent a car R, return a car U, of Quit Q?'
        answer = input(msg)
        while answer is not 'Q':
            if answer is 'R':
                msg = 'What type of car would you  like to rent?\
                       E for electric, P for petrol'
                carType = input(msg)
            answer = input('Would you like to rent a car R, ')
            if answer == 'Y':
                carType = input('Would you like to Rent R or Return T?')
            # etc. Stick it in a while look.


europcar = CarFleet()
