# gregorianEpact.py
#   This program determines the gregorian epact
#   which is the number of days between January 1st and the previous new moon
#   This value is used to figure out the date of Easter

def main():
    # Introduction
    print("This program determines the gregorian epact which is the number of days between January 1st and the previous new moon.")
    print("This value is used to figure out the date of Easter.")
    print()

    # Input
    year = int(input("Enter a 4-digit year: "))

    # Process
    C = year//100
    
    epact = (8+(C//4) - C + ((8*C + 13)//25) + 11*(year%19)) % 30

    # Output
    print("The value of the epact is",epact)
    
main()