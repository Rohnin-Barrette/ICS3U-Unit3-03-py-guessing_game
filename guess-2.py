#!/usr/bin/env python3

# Created by: Rohnin Barrette
# Created on: Sep 2021
# This function asks the user to guess a number between 1 and 10

import random


def main():
    # This function asks the user to guess a number between 1 and 9

    # input
    guessed_number = int(input("Enter a number between 1 and 10: "))
    print("")

    # process & output
    random_number = random.randint(1, 10)

    if guessed_number == random_number:
        print("YAAAAY you guessed it right!!!")
    else:
        print(" :( You got it wrong. Try again")

    print("\nDone.")


if __name__ == "__main__":
    main()
