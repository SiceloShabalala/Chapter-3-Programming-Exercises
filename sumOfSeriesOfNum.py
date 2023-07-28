# sumOfSeriesOfNum.py
#   This program sums a series of numbers provided by a user.
#   @author: Sicelokuhle Siyabonga Shabalala
#   @date: 22/07/2023

def main():
    # Introduction
    print("This program sums a series of numbers provided by a user.")
    print()

    # Input
    numbers = int(input("How many numbers are to be summed: "))

    # Process
    sum = 0
    for i in range(numbers):
        numberToSum = int(input("Enter number: "))
        sum = sum+numberToSum

    # Output
    print("The sum of the numbers entered is",sum)

main()