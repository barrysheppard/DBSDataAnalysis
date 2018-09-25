###############################################################################
# Programming Essentials B8IT102 Assessment                                   #
# Student: Barry Sheppard ID: 10387786                                        #
# Problem 4                                                                   #
###############################################################################


###############################################################################
# Import                                                                      #
###############################################################################
from problem4class import PhoneBook


###############################################################################
# Functions                                                                   #
###############################################################################
def PrintMenu():
    """ This function displays the options for the user to select from """
    print("")
    print("###################################")
    print("MYPY PHONE BOOK")
    print("###################################")
    print("1 : Add New Entry")
    print("2 : Delete Entry")
    print("3 : Update Entry")
    print("4 : Lookup Number")
    print("5 : QUIT")


###############################################################################
# Prompt the user for the required input                                      #
###############################################################################

# Create the phoneBook object as an instance of the PhoneBook class
phoneBook = PhoneBook()

# Promopt the user for a selection, any input but 1, 2, 3, 4, or 5 results in
# an error message. In some cases an additional option is required.
# The PhoneBook() class includes error checking
userSelection = ""
while userSelection is not "5":
    PrintMenu()
    userSelection = input()

    # 1 : Add New Entry
    if userSelection == "1":
        newNumber = input("Input a new number: ")
        newName = input("Input a new name: ")
        if phoneBook.AddNumber(newNumber, newName) is True:
            print("Details succesfully added.")
        else:
            print("Error:", phoneBook.AddNumber(newNumber, newName))

    # 2 : Delete Entry
    elif userSelection == "2":
        deleteNumber = input("Input the number to delete: ")
        if phoneBook.DeleteNumber(deleteNumber) is True:
            print("Number successfully deleted.")
        else:
            print("That number does not exist.")

    # 3 : Update Entry
    elif userSelection == "3":
        updateNumber = input("Input the number to update: ")
        updateName = input("Input the new name: ")
        if phoneBook.UpdateNumber(updateNumber, updateName) is True:
            print("Number successfully updated.")
        else:
            print("That number does not exist.")

    # 4 : Lookup Number
    elif userSelection == "4":
        nameOrNumber = ""
        while nameOrNumber is not "1" and nameOrNumber is not "2":
            print("1: Enter a name and get the number.")
            print("2: Enter a number and get the name.")
            nameOrNumber = input()
        # 4 : 1 Lookup Number based on Name
        if nameOrNumber == "1":
            lookupName = input("Enter name to lookup: ")
            result = phoneBook.LookupName(lookupName)
            if result is not False:
                print("The number is: ", result)
            else:
                print("That name is not listed.")
        # 4 : 2 Lookup Name based on Number
        elif nameOrNumber == "2":
            lookupNumber = input("Enter number to lookup: ")
            result = phoneBook.LookupNumber(lookupNumber)
            if result is not False:
                print("The name is: ", result)
            else:
                print("That name is not listed.")

    # 4 : Quit Program
    elif userSelection == "5":
        print("Good Bye!")

    # ?? : User did not enter a vaid selection
    else:
        print("You did not make a valid selection.")
