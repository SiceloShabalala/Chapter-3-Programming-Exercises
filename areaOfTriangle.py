# areaOfTriangle.py
#   This program calculates the area of a triangle given the length
#   of its three sides - a,b, and c.
#   @author: Sicelokuhle Siyabonga Shabalala
#   @date: 22/07/2023

import math

def main():
    # Introduction
    print("This program calculates the area of a triangle given the length of its three sides a,b,and c.")
    print()

    # Input
    a,b,c = eval(input("Enter the length of the three sides seperated by a comma ',': "))

    # Process
    s = (a+b+c)/2
    A = math.sqrt(s*(s-a)*(s-b)*(s-c))

    # Output
    print("The Area of the triangle is",A)

main()