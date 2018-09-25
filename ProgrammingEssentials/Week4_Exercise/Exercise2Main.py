# Week 4 Exercise 2 - Continued from Exercise2Classes.py
# In this file declare and initialise a dictionary. For example
# referenceDataDictionary = {1:"Personal",2:"Corporate",3:"Wholesale"}

newDictionary = {1: "Personal", 2: "Corporate", 3: "Wholesale"}

# Instantiate the Reference Data class and pass in the dictionary declared
# above into the constructor

from Exercise2Classes import referenceDataDictionary

dictionaryObject = referenceDataDictionary(newDictionary)

# Prompt the user to enter a key for which you will return the corresponding
# Reference Data Description. Your program must keep prompting the user for a
# numeric key until one is entered

# If the key does not exist you must let the user know.

# We set selection to a valid value, to star the loop
# but will prompt the user for a new input at the start of the loop

keep_asking = True

while keep_asking:
    try:
        x = int(input("Please enter a valid reference number: "))
        print("The reference is:", dictionaryObject.GetValueByKey(x))
        keep_asking = False
    except ValueError:
        print("The input was not an integer. Please try again...")
    except KeyError:
        print("That value does not exit. Please try again...")
    except Exception:
        print("There was an error. Please try again...")
