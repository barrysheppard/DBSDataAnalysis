###############################################################################
# Programming Essentials B8IT102 Assessment                                   #
# Student: Barry Sheppard ID: 10387786                                        #
# Problem 3                                                                   #
###############################################################################


###############################################################################
# Functions                                                                   #
###############################################################################

def CheckNumberIsInt(userInput):
    """ This function returns True if userInput can be converted to an int and
    returns False if it cannot. """
    try:
        int(userInput)
        return True
    except(ValueError):
        return False


###############################################################################
# Prompt the user for the required input                                      #
###############################################################################

# Print the intro message using triple " for multiline
print("""###################################
WELCOME TO THE DBS CONSOLE
###################################""")

# Ask the user for the number of elements Check this was a whole number.
# Re-ask if required.
keepAsking = True
message = "Input the number of elements to be stored in the list :"
while keepAsking:
    numElements = input(message)
    if CheckNumberIsInt(numElements):
        numElements = int(numElements)
        keepAsking = False
    else:
        print("Input was not an integer.")
print("Input", numElements, "elements in the list :")

# Create an empty list that we will add elements to
storedList = []

# We use a while loop repeating until the total number of elements have been
# stored
count = 0
while count < numElements:
    # As we only want to store integer values, the input rejects any values
    # the user inputs that are non-integers and reasks
    keepAsking = True
    while keepAsking:
        userInput = input("element - " + str(count) + " : ")
        if CheckNumberIsInt(userInput):
            keepAsking = False
        else:
            print("Input was not an integer.")
    storedList.append(userInput)
    count += 1


###############################################################################
# Calculations                                                                #
###############################################################################

# To count the frequncy we create a dictionary list for each time
frequencyData = {i: storedList.count(i) for i in storedList}

###############################################################################
# Display Output                                                              #
###############################################################################

# To return our the elements and frequency we use a for loop to go through
# the dictionary. To check grammar we use an if to check if there is 1 or more.
print("")
print("The frequency of all elements of the list :")
for item, count in frequencyData.items():
    if count == 1:
        times = "time"
    else:
        times = "times"
    print(item, "occurs", count, times)
