# sumOfFirstN.py
#   This program finds the sum of the first n natural numbers
#   @author: Sicelokuhle Siyabonga Shabalala
#   @date: 22/07/2023

def main():
    # Introduction
    print("This program finds the sum of the first n natural numbers")
    print()

    # Input
    n = int(input("Enter a Natural Number(n): "))

    # Process
    accumulator = 0
    for i in range(n,0,-1):
        accumulator = accumulator + i

    # Output
    if accumulator<=0:
        print("0 is not a natural number!")
    else:
        print("The sum of the first n natural numbers is",accumulator)

main()