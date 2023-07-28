# averageOfSeriesOfNum.py
#   This program provides the average of a series of numbers provided by a user.
#   @author: Sicelokuhle Siyabonga Shabalala
#   @date: 22/07/2023

def main():
    # Introduction
    print("This program provides the average of a series of numbers provided by a user.")
    print()

    # Input
    numbers = int(input("How many numbers are to be averaged: "))

    # Process
    sum = 0
    for i in range(numbers):
        numberToSum = int(input("Enter number: "))
        sum = sum+numberToSum

    average = sum/numbers
    # Output
    print("The average of the numbers entered is",average)

main()