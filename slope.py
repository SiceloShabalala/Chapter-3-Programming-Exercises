# slope.py
#   This program calculates the slope of a line through two (non-vertical) points
#   @author: Sicelokuhle Siyabonga Shabalala
#   @date: 22/07/2023

def main():
    # Introduction
    print("This Program to calculate the slope/gradient of a line through two non-vetical points")
    print()

    # Input
    pointx1, pointy1 = eval(input("Enter the 1st x and y points separated by a comma ',': "))
    pointx2, pointy2 = eval(input("Enter the 2nd x and y points separated by a comma ',': "))

    # Process
    slope = (pointy2 - pointy1)/(pointx2 - pointx1)

    # Output
    print("The slope of the line is",slope)

main()