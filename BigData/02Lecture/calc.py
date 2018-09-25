# This is the basics of our calculator. It is saved as calc.py


def add(first, second):
    ''' This returns the multiplication of two numbers '''
    return first + second


def multiply(first, second):
    ''' This returns the addition of two numbers '''
    return first * second


def divide(first, second):
    '''
    This returns the first number divided by the second number
    This will raise a divide by zero exception if second = 0
    '''
#    if second == 0:
#        return "Cannot divide by Zero"
    return first / second


def subtract(first, second):
    ''' This returns the first number less the second number '''
    return first - second


def exponent(first, second):
    ''' This returns the first number to the power of the second number '''
    return first ** second
