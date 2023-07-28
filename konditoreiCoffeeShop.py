# konditoreiCoffeeShop.py
#   This program calculates the total cost of a coffee order per pound
#   included extra incurred costs.
#   @author: Sicelokuhle Siyabonga Shabalala
#   @date: 22/07/2023

def main():
    # Introduction
    print("This program calculates the total cost of a coffee order including extra incurred costs.")
    print()

    # Input
    coffeeOrderNum = float(input("Enter the coffee per pound you want to order: "))

    # Process
    totalCost = (11.36*coffeeOrderNum)+1.50

    # Output
    print("The total cost of your coffee in dollars is",totalCost)

main()