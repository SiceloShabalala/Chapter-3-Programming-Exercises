# lightningStrike.py
#   This progrma determines the distance to a lightning strike
#   based on the time elapsed between  the flash and the sound of thunder.
#   The speed of sound is approximately 1100 ft/sec and 1 mile is 5380 ft
#   @author: Sicelokuhle Siyabonga Shabalala
#   @date: 22/07/2023

def main():
    #Introduction
    print("This progrma determines the distance to a lightning strike")
    print("based on the time elapsed between  the flash and the sound of thunder.")
    print()

    # Input
    time_elapsed = float(input("Enter the time elapsed between the flash and sound of thunder: "))

    # Process
    # 1 mile = 5280ft and speed of sound = 1100ft/sec
    time_elapsed_per_mile = 5280/1100
    distance_to_lightning_strike_in_miles = (1 * time_elapsed)/(time_elapsed_per_mile)
    distance_to_lightning_strike_in_feet = distance_to_lightning_strike_in_miles*5280

    # Output
    print("The distance to the lightning strike in feet is approximately", distance_to_lightning_strike_in_feet)

main()