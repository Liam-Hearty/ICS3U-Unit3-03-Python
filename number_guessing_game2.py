#!/usr/bin/env python3

# Created by: Liam Hearty
# Created on: September 2019
# This program makes the user guess the random number.


import constants


def main():
    # This program makes the user guess the random number.

    # input
    chosen_number = int(input("Enter your guess between 0-9: "))

    # process
    if chosen_number == constants.random_number:
        # output
        print("Correct!!")

    else:
        print("Wrong! the number was:{0} ".format(constants.random_number))


if __name__ == "__main__":
    main()
