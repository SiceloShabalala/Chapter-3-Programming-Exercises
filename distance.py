# slope.py
#   This program calculates the distance between two points
#   @author: Sicelokuhle Siyabonga Shabalala
#   @date: 22/07/2023
import math

def main():
    # Introduction
    print("This program calculates the distance between two points")
    print()

    # Input
    pointx1, pointy1 = eval(input("Enter the 1st x and y points separated by a comma ',': "))
    pointx2, pointy2 = eval(input("Enter the 2nd x and y points separated by a comma ',': "))

    # Process
    distance = math.sqrt(math.pow((pointx2 - pointx1),2) + math.pow((pointy2 - pointy1),2))

    # Output
    print("The distance between the two points is",distance)

main()