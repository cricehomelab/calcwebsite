from mathtest.utils import math_functions
import math

# tests to ensure we can get a float to do math with. 
def test_ensure_int():
    assert math_functions.ensure_float(5)    == 5
    assert math_functions.ensure_float("5")  == 5
    assert math_functions.ensure_float(".5") == .5

# test with things that will not work. 
def test_cannot_int():
    assert math_functions.ensure_float("f")    == "invalid number"  
    assert math_functions.ensure_float("five") == "invalid number"
    assert math_functions.ensure_float("")     == "invalid number"
    assert math_functions.ensure_float(" ")    == "invalid number"
    assert math_functions.ensure_float("=")    == "invalid number"

# Test multiplication testing some numbers out that will give us a good value.
def test_multiply():
    assert math_functions.multiply("3", "5")   == 15.0
    assert math_functions.multiply(".5", "10") == 5.0
    assert math_functions.multiply("5", 10)    == 50.0
    assert math_functions.multiply(3, 6)       == 18.0    
    assert math_functions.multiply(1, .5)      == 0.5

# Test multiplication that should fail to give a number.
def test_fail_multipy():
    assert math_functions.multiply("five", 3)       == "invalid number"
    assert math_functions.multiply(4, "five")       == "invalid number"
    assert math_functions.multiply("3", "fifteen")  == "invalid number"
    assert math_functions.multiply("four", "3")     == "invalid number"
    assert math_functions.multiply("four", "three") == "invalid number"

# Test division that should be successful.
def test_divide():
    assert math_functions.divide("10", "2") == 5.0
    assert math_functions.divide("1", "3")  == (1 / 3)
    assert math_functions.divide("1", "2")  == 0.5
    assert math_functions.divide(100, 50)   == 2.0
    assert math_functions.divide("3", 6)    == .5
    assert math_functions.divide(4, "5")    == .8

# Test division that should fail. 
def test_fail_divide():
    assert math_functions.divide("five", "three") == "invalid number"
    assert math_functions.divide("3", "five")     == "invalid number"
    assert math_functions.divide("five", "3")     == "invalid number"
    assert math_functions.divide("=", "3")        == "invalid number"
    assert math_functions.divide("6", "-")        == "invalid number"

# Test additions that should be successful. 
def test_add():
    assert math_functions.add("2", "3") == 2 + 3
    assert math_functions.add(2, "3")   == 2 + 3
    assert math_functions.add("3", 2)   == 3 + 2
    assert math_functions.add(5, 5)     == 5 + 5

# Test additions that should fail. 
def test_fail_add():
    assert math_functions.add("five", "three") == "invalid number"
    assert math_functions.add("3", "five")     == "invalid number"
    assert math_functions.add("five", "3")     == "invalid number"
    assert math_functions.add("=", "3")        == "invalid number"
    assert math_functions.add("6", "-")        == "invalid number"

# Test subtractions that should be successful.
def test_subtract():
    assert math_functions.subtract("10", "5")    == 10 - 5
    assert math_functions.subtract("10", "0")    == 10 - 0
    assert math_functions.subtract("5", "10")    == 5 - 10
    assert math_functions.subtract("5.5", "5.1") == 5.5 - 5.1
    assert math_functions.subtract("5", 5)       == 5 - 5
    assert math_functions.subtract(5, "5")       == 5 - 5
  
# Test subractions that should fail.
def test_fail_subtract():
    assert math_functions.subtract("five", "three") == "invalid number"
    assert math_functions.subtract("3", "five")     == "invalid number"
    assert math_functions.subtract("five", "3")     == "invalid number"
    assert math_functions.subtract("=", "3")        == "invalid number"
    assert math_functions.subtract("6", "-")        == "invalid number"

# Tests a square function ie x ^ 2 or x ** 2 to fit syntactically. 
def test_square():
    assert math_functions.square("1") == 1.0 ** 2.0
    assert math_functions.square(1)   == 1.0 ** 2.0
    assert math_functions.square("2") == 2.0 ** 2.0
    assert math_functions.square(2)   == 2.0 ** 2.0
    assert math_functions.square(4)   == 4.0 ** 2.0

# tests squares that will fail for sure.
def test_fail_square():
    assert math_functions.square("one")  == "invalid number"
    assert math_functions.square("=")    == "invalid number"
    assert math_functions.square("g")    == "invalid number"

# test exponents.
def test_expontent():
    assert math_functions.exponent("2", "2") == 2 ** 2
    assert math_functions.exponent("2", "3") == 2 ** 3
    assert math_functions.exponent(2, 2)     == 2 ** 2
    assert math_functions.exponent(2, "3")   == 2 ** 3
    assert math_functions.exponent("3", 5)   == 3 ** 5

# Test Exponents all these should fail in a calculator.
def test_fail_exponent():
    assert math_functions.exponent("two", "3") == "invalid number"
    assert math_functions.exponent("two", 3)   == "invalid number"
    assert math_functions.exponent("3", "two") == "invalid number"
    assert math_functions.exponent(3, "two")   == "invalid number"
    assert math_functions.exponent("=", "3")   == "invalid number"

# test squareroots
def test_squareroot():
    assert math_functions.squareroot("3") == math.sqrt(3)
    assert math_functions.squareroot(3)   == math.sqrt(3)
    assert math_functions.squareroot(8)   == math.sqrt(8)
    assert math_functions.squareroot("9") == math.sqrt(9)

# test squareroots that will not work. 
def test_fail_squareroot():
    assert math_functions.squareroot("-1")  == "invalid number"
    assert math_functions.squareroot("-10") == "invalid number"
    assert math_functions.squareroot(-1)    == "invalid number"
    assert math_functions.squareroot(-10)   == "invalid number"

# test sine values degree is the unit of measure being entered. 
def test_sine_degrees():
    assert math_functions.sine_degrees("0") == 0
    assert math_functions.sine_degrees("90") == 1
    assert math_functions.sine_degrees("180") == 0
    assert math_functions.sine_degrees("270") == -1

# test cosine values degree is the unit of measure being entered. 
def test_cosine_digrees():
    assert math_functions.cosine_degrees("0") == 1
    assert math_functions.cosine_degrees("90") == 0
    assert math_functions.cosine_degrees("180") == -1
    assert math_functions.cosine_degrees("270") == 0


