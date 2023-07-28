# approximationOfPi.py
#   This program approximates the value of pi by summing the terms of this series:
#   4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + ...

import math

def main():
    # Introduction
    print("This program approximates the value of pi by summing the terms of this series:")
    print("4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + ...")
    print()

    # Input
    n = int(input("Enter the number of terms to sum(n): "))

    denominator = 1

    sum = 0
    for i in range(n):
        if(i % 2 == 0):
            sum = sum + (4/denominator)

        else:
            sum = sum + (-1*(4/denominator))

        denominator = denominator + 2

    print("The sum of the series for",n,"terms is",sum)
    approximation = math.pi - sum
    print()
    print("Accuracy of the sum of terms approximating pi is",approximation)

main()