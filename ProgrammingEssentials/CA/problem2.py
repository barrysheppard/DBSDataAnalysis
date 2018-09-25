###############################################################################
# Programming Essentials B8IT102 Assessment                                   #
# Student: Barry Sheppard ID: 10387786                                        #
# Problem 2                                                                   #
###############################################################################


###############################################################################
# Prompt the user for the required input                                      #
###############################################################################

# Print the intro message using triple " for multiline
print("""###################################
WELCOME TO THE DBS CONSOLE
###################################""")

# Ask user to input their username
keepAsking = True
while keepAsking:
    print("Please enter your username:")
    username = input()
    # Need to check the input has exactly 1 \ character
    # As this is an escape character we need to include it twice
    usernameSplit = username.split(sep="\\")
    if len(usernameSplit) is not 2:
        # The r before the text indicates raw to make sure the \ displays
        print(r"The username must be in the format domain \ name")
    else:
        keepAsking = False


###############################################################################
# Calculations                                                                #
###############################################################################

# Assign the domain and username variables assuming they will be needed later
domain = usernameSplit[0]
username = usernameSplit[1]


###############################################################################
# Display Output                                                              #
###############################################################################

# Print the Domain and Username as separate entries
print("")
print("Domain : ", domain)
print("Username : ", username)
print("")
