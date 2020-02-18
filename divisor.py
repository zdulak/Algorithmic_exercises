import sys


def gcd(num1, num2):
    """ Euclid's algorithm for finding the greatest common divisor of two numbers. """
    while num2 != 0:
        r = num1 % num2
        num1 = num2
        num2 = r
    return num1


try:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    print("The greatest common divisor of", num1, "and", num2, "is equal", gcd(num1, num2))
except (IndexError, ValueError):
    print("Please enter two integer numbers in the command line.")
