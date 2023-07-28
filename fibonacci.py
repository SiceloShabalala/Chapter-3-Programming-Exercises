# fibonacci.py
#   This program implements the fibonacci sequence.
#   The fibonacci sequence is a sequence of numbers where each successive number is the sum of the previous two.
#   @author: Sicelokuhle Siyabonga Shabalala
#   @date: 22/072023

def main():
    # Introduction
    print("This program implements the fibonacci sequence:")
    print("It's a sequence of numbers where each successive number is the sum of the previous two.")
    print()

    # Input
    n = int(input("Enter the nth term to be computed: "))

    # Process
    first = 0
    second = 0
    sum = 0
    for i in range(n):
        if i == 0 or i == 1:
            first = 1
            second = 1
            sum = 1
        
        else:
            sum = first+second
            second = sum
            first = sum - first

    # Output
    print("The nth Fibonacci number is",sum)
    
main()