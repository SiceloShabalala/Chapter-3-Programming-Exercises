# molecularWeight.py
#   This program computes the molecular weight of a carbohydrate (in grams per mole)
#   based on the number of hydrogen, carbon, and oxygen atoms in the molecule.
#   Program prompts user to enter the number of hydrogen atoms, carbon atoms, and oxygen atoms.
#   Program then prints the total combined molecular weight of all the atoms based on these
#   individual atom weights.

def main():
    # Introduction
    print("This program computes the molecular weight of a carbohydrate (in grams per mole)")
    print("based on the number of hydrogen, carbon, and oxygen atoms in the molecule.")
    print("Program prompts user to enter the number of hydrogen atoms, carbon atoms, and oxygen atoms.")
    print("Program then prints the total combined molecular weight of all the atoms based on these")
    print("individual atom weights.")
    print()
    
    # Input
    hydrogen = float(input("Enter the number of Hydrogen atoms in the molecule: "))
    carbon = float(input("Enter the number of Carbon atoms in the molecule: "))
    oxygen = float(input("Enter the number of Oxygen atoms in the molecule: "))

    # Process
    hMolecularWeight = hydrogen * 1.00794
    cMolecularWeight = carbon * 12.0107
    oMolecularWeight = oxygen * 15.9994
    totalMolecularWeight = hMolecularWeight + cMolecularWeight + oMolecularWeight

    # Output
    print("The total molecular weight of the atoms in grams per mole is",totalMolecularWeight)

main()