# Week 4 Exercise 3 - Continued from Exercise3Classes.py

from Exercise3Classes import Association

# In this file declare and initialise a dictionary with all the Association
# Types from your Database. For example.

associationTypesDictionary = {7: "Consultant", 8: "Therapist", 9: "Surveyor"}

# Prompt the user for all values you  need to create the Association. On
# capturing the Assosciation Type you must resolve this to an Association Type
# ID by looking up the dictionary you declared If the user enters an invalid
# Association Type, keep prompting

# Prompt user for the first customer id name.
# Check to make sure if the name is less than 50 characters
keep_asking = True
while keep_asking:
    customerName = input("Please enter name for new assocation: ")
    if len(customerName) > 50:
        print("The name must be 50 characters or less")
    else:
        keep_asking = False

# Prompt user for the first customer id number
keep_asking = True
while keep_asking:
    try:
        customerId1 = int(input("Please enter customer 1 id: "))
        keep_asking = False
    except ValueError:
        print("The input was not an integer. Please try again...")
    except Exception:
        print("There was an error. Please try again...")

# Prompt user for the second customer id number
keep_asking = True
while keep_asking:
    try:
        customerId2 = int(input("Please enter customer 2 id: "))
        keep_asking = False
    except ValueError:
        print("The input was not an integer. Please try again...")
    except Exception:
        print("There was an error. Please try again...")


# Adding a function to get the key from a dictionary using a value
def find_key(input_dict, value):
    return next((k for k, v in input_dict.items() if v == value), False)


# Prompt user for the association checking it is valid
keep_asking = True
while keep_asking:
    association = input("Please enter association type: ")
    if find_key(associationTypesDictionary, association) is not False:
        associationTypeId = find_key(associationTypesDictionary, association)
        keep_asking = False
    else:
        print("There was an error. Please try again...")

# Implement exception handling in  your class so that any errors that arise
# are caught and rised back up to the calling code.

# Lets create the association object.
assoc = Association(customerName, customerId1, customerId2, associationTypeId)

# Some output code to check we're doing this correctly
print("New Customer Name is:", assoc.GetName())
print("Customer ID 1 is:", assoc.GetCustomer1())
print("Customer ID 2 is:", assoc.GetCustomer2())
print("Association Type is:", assoc.GetAssociationTypeId())

# Last we commit to the database
assoc.CreateAssociation()

print("Association Created")
