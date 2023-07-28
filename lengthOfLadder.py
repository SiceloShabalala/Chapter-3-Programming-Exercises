# lengthOfLadder.py
#   This program determines the length of a ladder required to reach
#   a given height when leaned against a house.
#   The height anf angle of the ladder are given as inputs.

import math

def main():
    # Introduction
    print("This program determines the length of a ladder required to reach")
    print("a given height when leaned against a house.")
    print()

    # Input
    height, angle = eval(input("Enter the height and angle of the ladder is that sequence, seperated by a comma ',': "))

    # Process
    radians = angle * (math.pi/180)
    length = height/(math.sin(radians))

    # Output
    print("The length of the ladder is",length,"units")

main()