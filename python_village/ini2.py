#!/usr/bin/env python3

"""
Author : Nathalia Graf Grachet
Date   : 2021-01-15
Purpose: Python Village - Variables and Some Arithmetic
"""

import argparse


class BadIntegerValue(Exception):
    """Base class for other exception """


# --------------------------------------------------
def get_args():
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description="""Variables and Some Arithmetic. Given two integers,
        a and b, each less than 1000, this program returns the square of the
        hypothenuse of the right triangle whose legs have lenghts a and b.""",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('input_file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        help='Input file, max 2 integers')

    args = parser.parse_args()

    return args.input_file.read().rstrip().split()


# --------------------------------------------------
def main():
    """Returns the square of the hypothenuse of a triangle
    with a and b legs"""

    args = get_args()
    list_int = [int(x) for x in args]

    for i in list_int:
        test_int(i)

    a, b = list_int

    h = (a*a) + (b*b)

    print(h)


# --------------------------------------------------
def test_int(v):
    """Test if integer v is less than 1000"""

    if v >= 1000:
        raise BadIntegerValue("Integer must be less than 1000.")


# --------------------------------------------------
if __name__ == '__main__':
    main()
