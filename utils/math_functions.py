import math

# converts the number from string to float as long as it is able to be
# converted to one. 
def ensure_float(num):
    '''This ensures the input, num, is  floating point number.'''
    if type(num) == type("string"):
      try:
          return float(num)
      except ValueError:
          return "invalid number"
    else:
        return float(num)

# takes 2 numbers and multiplys the result. 
def multiply(num1, num2):
    '''returns the product of num1 and num2.'''
    num1 = ensure_float(num1)
    num2 = ensure_float(num2)
    if (num1 == "invalid number" or num2 == "invalid number"):
        return "invalid number"
    else:
        return num1 * num2

# takes two numbers and divides the first numbe num1 by the second number num2.
def divide(num1, num2):
    '''num1 = dividend, num2 = divisor. Returns the quotient.'''
    num1 = ensure_float(num1)
    num2 = ensure_float(num2)
    if (num1 == "invalid number" or num2 == "invalid number"):
        return "invalid number"
    else:
        return num1 / num2

# takes two numbers and gives us the sum of the numbers. 
def add(num1, num2):
    '''returns the sum of num1 and num2.'''
    num1 = ensure_float(num1)
    num2 = ensure_float(num2)
    if (num1 == "invalid number" or num2 == "invalid number"):
        return "invalid number"
    else:
        return num1 + num2

# gives us the product of num1 - num2.
def subtract(num1, num2):
    '''sum1 = minuend, sum2 = subtrahend, returns the difference.'''
    num1 = ensure_float(num1)
    num2 = ensure_float(num2)
    if (num1 == "invalid number" or num2 == "invalid number"):
       return "invalid number"
    else:
        return num1 - num2

# gives us the square of two numbers. 
def square(num1):
    '''returns the value of num1 squared.'''
    num1 = ensure_float(num1)
    if (num1 == "invalid number"):
        return "invalid number"
    else:
        return num1 ** 2.0

# puts out the result of num1 to the num2 power. 
def exponent(num1, num2):
    '''returns the value of num1 to the num2 power.'''
    num1 = ensure_float(num1)
    num2 = ensure_float(num2)
    if (num1 == "invalid number" or num2 == "invalid number"):
       return "invalid number"
    else:
        return num1 ** num2

# takes the square root of num1.
def squareroot(num1):
    '''returns the square root of num1.'''
    num1 = ensure_float(num1)
    if (num1 == "invalid number"):
        return "invalid number"
    else:
        if num1 > 0:
            return math.sqrt(num1)
        else:
            return "invalid number"

def sine_degrees(num1):
    pass


def cosine_degrees(num1):
    pass
