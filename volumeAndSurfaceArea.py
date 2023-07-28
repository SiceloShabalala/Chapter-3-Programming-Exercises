# volumeAndSurfaceArea.py
#   This program calculates the volume and surface area of a sphere given it's radius as input
#   @author: Sicelokuhle Siyabonga Shabalala
#   @date: 21/07/2023

import math

def main():
    # Introduction
    print("This program calculates the volume and surface area of a sphere given it's radius as input.")

    # Input
    radius = float(input("Enter the radius of the sphere: "))

    # Process
    volume = 4/3 * math.pi * math.pow(radius,3)
    Area = 4 * math.pi * math.pow(radius,2)

    # Output
    print("The volume of the sphere is",volume,"units cubed")
    print("The Area of the sphere is", Area,"units squared")
    
main()