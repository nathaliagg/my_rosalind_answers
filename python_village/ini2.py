#!/usr/bin/env python3

"""
Author : Nathalia Graf Grachet
Date   : 2021-01-15
Purpose: Python Village - Variables and Some Arithmetic
"""

import argparse


# --------------------------------------------------
def get_args():
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description="""Variables and Some Arithmetic. Given two integers,
        a and b, each less than 1000, this program returns the square of the
        hypothenuse of the right triangle whose legs have lenghts a and b.""",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('int_a',
                        metavar='int',
                        type=int,
                        choices=range(1, 1001),
                        help='Integer a < 1000')

    parser.add_argument('int_b',
                        metavar='int',
                        type=int,
                        choices=range(1, 1001),
                        help='Integer b < 1000')

    args = parser.parse_args()

    return args


# --------------------------------------------------
def main():
    """Returns the square of the hypothenuse of a triangle
    with a and b legs"""

    args = get_args()
    # print(args)

    a = args.int_a
    b = args.int_b

    h = (a*a) + (b*b)

    print(h)


# --------------------------------------------------
if __name__ == '__main__':
    main()
