###############################################################################
# Programming Essentials B8IT102 Assessment                                   #
# Student: Barry Sheppard ID: 10387786                                        #
# Problem 4 Class File                                                        #
###############################################################################


# Create a Class called PhoneBook
class PhoneBook():

    # This class has just one variable, a list of phone numbers in a dictionary
    __dictionaryOfNumbers = {}

    def LookupNumber(self, phoneNumber):
        """ To access a name from a number we use this function
            If no value is found, the method returns False """
        try:
            return self.__dictionaryOfNumbers[phoneNumber]
        except Exception:
            return False

    def LookupName(self, phoneName):
        """ To access a number from a name we use this function
            If the name provided is not found the method returns False """
        try:
            return next((k for k, v in self.__dictionaryOfNumbers.items()
                         if v == phoneName), False)
        except Exception:
            return False

    def AddNumber(self, phoneNumber, phoneName):
        """ To add a new phone number and name we use this function.
            If successful the method returns True.
            If the number already exists the method returns
            'Phone number already exists'.
            If the number is actually a number the method returns
            'Phone number not a valid number'
            If the number has too few characters (< 5) the method returns
            'Phone number is too short'.
            If the number has too many characters (> 15) the method returns
            """
        # Check if phoneNumber is a number
        if self.__CheckNumberIsInt(phoneNumber):
            if self.LookupNumber(phoneNumber) is False:
                # Check if phoneNumber length is between 5 and 15
                if 4 < len(phoneNumber) < 16:
                    self.__dictionaryOfNumbers[phoneNumber] = phoneName
                    return True
                else:
                    return "Phone number must be between 5 and 15 numerals."
            else:
                return "Phone number already exists."
        else:
            return "Phone number must only contain numerals."

    def DeleteNumber(self, phoneNumber):
        """  To delete a phone number we use this function.
             If succesful the method returns True.
             If the number does not exist the method returns False"""
        if self.LookupNumber(phoneNumber) is not False:
            del self.__dictionaryOfNumbers[phoneNumber]
            return True
        else:
            return False

    def UpdateNumber(self, phoneNumber, newName):
        """  To update a number we use this function.
             If successful the method returns True.
             If the number does not exist the method returns False"""
        if self.LookupNumber(phoneNumber) is not False:
            self.__dictionaryOfNumbers[phoneNumber] = newName
            return True
        else:
            return False

    def __CheckNumberIsInt(self, input):
        """ Returns True if input can be converted to an int, otherwise False
        """
        try:
            int(input)
            return True
        except(ValueError):
            return False
