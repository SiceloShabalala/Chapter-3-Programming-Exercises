# costPerSquareInch.py
#   This program calculates the cost per square inch of a pizza given it's price and diameter
#   Input, Process, and Output Pattern
#   @author: Sicelokuhle Siyabonga Shabalala
#   @date: 21/07/2023

import math

def main():
    # Introduction
    print(" This program calculates the cost per square inch of a pizza given it's price and diameter!")
    print()

    # Input
    diameter = float(input("Enter the diameter of the pizza: "))
    price = float(input("Enter the cost price of the pizza: "))

    # Process
    area = math.pi * (diameter/2)
    costPerSquareInch = price/area

    # Output
    print("The cost per square inch of the pizza is",costPerSquareInch)

main()