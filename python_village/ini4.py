#!/usr/bin/env python3

"""
Author : Nathalia Graf Grachet
Date   : 2021-01-15
Purpose: Python Village - Conditionals and Loops
"""

import argparse


# define Python user-defined exceptions
class IntegerValueError(Exception):
    """Base class for other exceptions"""


# --------------------------------------------------
def get_args():
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description="""Conditionals and Loops. Given two positive integers,
        a < b < 10000, this program returns the sum of all odd integers from
        a through b, inclusively.""",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('int_a',
                        metavar='int',
                        type=int,
                        help='Integer a, a < b')

    parser.add_argument('int_b',
                        metavar='int',
                        type=int,
                        help='Integer b, b < 10000')

    args = parser.parse_args()

    return args


# --------------------------------------------------
def main():
    """Does it all"""

    args = get_args()
    # print(args)

    test_integers(args.int_a, args.int_b)

    print(sum_of_odds(args.int_a, args.int_b))


# --------------------------------------------------
def test_integers(a, b):
    """Test if a < b < 10000"""

    if b > 10000:
        raise IntegerValueError(f" b, {b}, must be less than 10000")

    if a > b:
        raise IntegerValueError(f"a, {a}, must be less than {b}")


# --------------------------------------------------
def sum_of_odds(a, b):
    """Take the sum of all odd numbers within a and b, inclusively"""

    s = 0

    for i in range(a, b+1):
        if i % 2 == 1:
            s += i
        else:
            continue

    return s


# --------------------------------------------------
if __name__ == '__main__':
    main()
