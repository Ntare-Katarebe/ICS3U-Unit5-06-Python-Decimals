#!/usr/bin/env python3

# Created by: Ntare Katarebe
# Created on: May 2021
# This program uses a decimal places you want to round off to

import math


def decimal_r(number):
    # function adds 1, by reference
    r_decimal = float(number[0] * pow(10, number[1]) + 0.5)
    r_integer = int(r_decimal)
    r_number = r_integer / pow(10, number[1])
    number[0] = r_number


def main():
    # this function gets a number and calls the add_one function
    numbers = input("Enter the number you want to round: ")
    decimals = input("Enter how many decimal places you want to round by: ")

    try:
        n_integer = float(numbers)
        d_integer = int(decimals)

        inputs = []
        inputs.append(n_integer)
        inputs.append(d_integer)
        decimal_r(inputs)
        print("\nThe rounded number is {}".format(inputs[0]))
    except Exception:
        print("\n{} this value is invalid".format(numbers))


if __name__ == "__main__":
    main()
