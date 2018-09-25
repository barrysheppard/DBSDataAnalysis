# Week 4 Exercise 2
# Create a class name ReferenceData. It's __init__() constructor should take
# self, and referenceDataDictionary as parameters. Make sure to set the
# member variables appropriately in the body of the __init_() method.


class referenceDataDictionary():
    """ This class is used to work with a dictionary """

    __dictionary = None

    def __init__(self, referenceDataDictionary):
        self.__dictionary = referenceDataDictionary

    # In your ReferenceData class create a function caled GetValueByKey. This
    # function will take two parameters: self and a key. Use the key to return
    # the corresponding description in the referenceDataDictionary.

    def GetValueByKey(self, key):
        return self.__dictionary[key]

# Create a separate python file in Visual studio where you will call the Class
# from. -- Continued in Exercise2Main.py
