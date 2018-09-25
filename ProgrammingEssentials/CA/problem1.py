###############################################################################
# Programming Essentials B8IT102 Assessment                                   #
# Student: Barry Sheppard ID: 10387786                                        #
# Problem 1                                                                   #
###############################################################################


###############################################################################
# Functions                                                                   #
###############################################################################

def LimitedInput(message, limit, isNumber=False):
    """ Prompt user for input and continue to do so until input is valid.

    This function takes two required inputs, the message to display, and the
    limit of characters required. If the user enters something too long, they
    are prompted again until the input is correct.
    If the optional isNumber parameter is True, then it will also continue to
    prompt the user until a valid number is input.

    """
    keepAsking = True
    while keepAsking:
        answer = input(message)
        if len(answer) > limit:
            print("The input must be", limit, "characters or less.")
        else:
            keepAsking = False
        if isNumber is True and CheckNumber(answer) is False:
            print("The input must be a number.")
            keepAsking = True
    return answer


def CheckNumber(userInput):
    """ This function returns True if userInput can be converted to a number and
    returns False if it cannot. """
    try:
        float(userInput)
        return True
    except(ValueError):
        return False


def DateInput(message):
    """ This function prompts the user for a date using the message variable.
    User will continue to be prompted until the format is correct.

    The date format is very specific in the format DD/MM/YYYYY
    This function will confirm there are the right number of characters,
    the / are in the right place, the input are numbers, the days are between
    1 and 31, the months are between 1 and 12, and the year is between 2000
    and 3000 (roll on year 3k bug!)
    """
    askAgainMessage = "The date must be in the format DD/MM/YYYY"
    keepAsking = True
    while keepAsking:
        answer = input(message)
        # First we check if there are two / by splitting using / and looking
        # for 3 items in the returned list.
        dateCheck = answer.split(sep="/")
        if len(dateCheck) is not 3:
            print(askAgainMessage)
        else:
            # If all is order, we can assign the 3 items to day, month, year
            day = dateCheck[0]
            month = dateCheck[1]
            year = dateCheck[2]
            # Next we check each item has the right amount of characters
            # and they can all be converted into numbers.
            if (len(day) == 2 and len(month) == 2 and len(year) == 4 and
                CheckNumber(day) and CheckNumber(month) and
                    CheckNumber(year)):
                day = int(day)
                month = int(month)
                year = int(year)
                if (day > 0 and day < 32 and month > 0 and month < 13 and
                        year > 2000 and year < 3000):
                    keepAsking = False
                else:
                    print(askAgainMessage)
            else:
                print(askAgainMessage)
    return answer


###############################################################################
# Prompt the user for the required input                                      #
###############################################################################

# Ask the user to input the required details
employeeName = LimitedInput("Employee Name: ", 20)  # Example Mark Bate
employeeNumber = LimitedInput("Employee Number: ", 10)  # Example 123456789A
weekEnding = DateInput("Week ending: ")  # Example 26/01/2018
hoursWorked = LimitedInput("Number of hours worked: ", 6, True)  # Example 42.5

# As there are only 168 hours in the week this is a check to prevent errors
# This could be modified to a lower number based on legal limit
while float(hoursWorked) > 168:
    print("The number of hours worked is too large.")
    hoursWorked = LimitedInput("Number of hours worked: ", 6, True)

standardRate = LimitedInput("Hourly Rate: ", 6, True)  # Example 10.50
overtimeMultiplier = LimitedInput("Overtime Rate: ", 3, True)  # Example 1.5
standardTaxRate = LimitedInput("Standard Tax Rate: ", 2, True)  # Example 20
overtimeTaxRate = LimitedInput("Overtime Tax Rate: ", 2, True)  # Example 50

# Cnvert input to numbers, during the input we validated these as numerals
hoursWorked = float(hoursWorked)
standardRate = float(standardRate)
overtimeMultiplier = float(overtimeMultiplier)
standardTaxRate = float(standardTaxRate)
overtimeTaxRate = float(overtimeTaxRate)


###############################################################################
# Calculate required details for ouput                                        #
###############################################################################

# Check if more than standard hours have been worked
if hoursWorked > 37.50:
    standardHours = 37.50
    overtimeHours = hoursWorked - 37.50
else:
    standardHours = hoursWorked
    overtimeHours = 0
# Complete additional calculations for pay and deductions
standardPayTotal = standardHours * standardRate
overtimeRate = overtimeMultiplier * standardRate  # As overtime is multiplier
overtimePayTotal = overtimeHours * overtimeRate
standardTaxTotal = (standardPayTotal * standardTaxRate)/100
overtimeTaxTotal = (overtimePayTotal * overtimeTaxRate)/100
payTotal = standardPayTotal + overtimePayTotal
totalDeductions = standardTaxTotal + overtimeTaxTotal
netPay = payTotal - totalDeductions


###############################################################################
# Printing out the Payslip                                                    #
###############################################################################

# Output is one big chunk of text with the variables inserted using the format
# function, this lets us define the float variables as two digit decimals.

print("""
                          P A Y S L I P
WEEK ENDING {:}
Employee: {:}
Employee Number: {:}
                      Earnings               Deductions
                      Hours   Rate   Total
Hours (normal)       {:6.2f}  {:6.2f}  {:6.2f}  Tax @ {:02.0f}% {:6.2f}
Hours (overtime)     {:6.2f}  {:6.2f}  {:6.2f}  Tax @ {:02.0f}% {:6.2f}

                      Total pay:                      {:7.2f}
                      Total deductions:               {:7.2f}
                      Net pay:                        {:7.2f}
""".format(weekEnding, employeeName, employeeNumber, standardHours,
           standardRate, standardPayTotal, standardTaxRate, standardTaxTotal,
           overtimeHours, overtimeRate, overtimePayTotal, overtimeTaxRate,
           overtimeTaxTotal, payTotal, totalDeductions, netPay))
