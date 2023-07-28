# sqrtNewtonsMethod.py
#   This program implements Newton's Method to determine the square root of a number.
#   @author: Sicelokuhle Siyabonga Shabalala
#   @date: 22/07/2023

import math
def main():
    # Introduction
    print("This program implements Newton's Method to determine the square root of a number.")
    print()

    # Input
    x,times = eval(input("Enter number to find square root of, and the number of times to improve the guess seperated by a comma value: "))

    # Process
    actualValue = math.sqrt(x)

    guess = x/2
    for i in range(times):
        guess = (guess + (x/guess))/2

    approximation = guess - actualValue

    # Output
    print("The final value of Guess is",guess)
    print("The approximation to the actual square root value is",approximation)
    
main()