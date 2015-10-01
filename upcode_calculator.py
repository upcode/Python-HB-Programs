#created functions for each arithmetic operator for calcuator interface


# add(int, int) → int
def add(num1, num2):
    """Returns the sum of the two input integers"""
    print num1 + num2
    return int(num1) + int(num2)


# subtract(int, int) → int
def subtract(num1, num2):
    """Returns the second number subtracted from the first"""
    print num1 - num2
    return int(num1) - int(num2)


# multiply(int, int) → int
def multiply(num1, num2):
    """Multiplies the two inputs together"""
    print num1 * num2
    return int(num1) * int(num2)


# divide(int, int) → float
def divide(num1, num2):
    """Divides the first input by the second, returning a floating point"""
    print num1 / num2
    return float(int(num1)) / float(int(num2))


# square(int) → int
def square(num1):
    """Returns the square of the input"""
    print num1 ** num1
    return int(num1) * int(num1)


# cube(int) → int
def cube(num1):
    """Returns the cube of the input"""
    print num1 ** 3
    return int(num1) ** 3


# power(int, int) → int
def power(num1, num2):
    """Raises the first integer to the power of the second integer and returns the value."""
    print int(num1) ** int(num2)
    return int(num1) ** int(num2)


# mod(int, int) → int
def mod(num1, num2):
    """Returns the remainder when the first integer is divided by the second integer."""
    print num1 % num2
    return int(num1) % int(num1)