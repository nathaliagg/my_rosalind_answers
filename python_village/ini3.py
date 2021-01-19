#!/usr/bin/env python3

"""
Author : Nathalia Graf Grachet
Date   : 2021-01-15
Purpose: Python Village - Strings and Lists
"""

import argparse


# define Python user-defined exceptions
class LengthString(Exception):
    """Base class for other exceptions"""


# --------------------------------------------------
def get_args():
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description="""Strings and Lists. Given a string s of maximum length
        of 200 letters, and four integers a, b, c, and d, this program returns
        two slices of the string from indices a through b, and
        c through d, inclusively.""",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('a_string',
                        metavar='str',
                        type=str,
                        help='A string < 200 letters')

    parser.add_argument('int_a',
                        metavar='int',
                        type=int,
                        help='Integer a')

    parser.add_argument('int_b',
                        metavar='int',
                        type=int,
                        help='Integer b')

    parser.add_argument('int_c',
                        metavar='int',
                        type=int,
                        help='Integer c')

    parser.add_argument('int_d',
                        metavar='int',
                        type=int,
                        help='Integer d')

    args = parser.parse_args()

    return args


# --------------------------------------------------
def main():
    """Slice string s, a through b, and
    c through d, inclusively."""

    args = get_args()
    # print(args)

    test_length_string(args.a_string)

    print(make_slices(args.a_string, args.int_a, args.int_b,
                      args.int_c, args.int_d))


# --------------------------------------------------
def test_length_string(s):
    """Test length of string, return error if > 200 letters"""

    if len(s) >= 200:
        raise LengthString(f"Lenght of string {len(s)} must be less than 200")


# --------------------------------------------------
def make_slices(s, a, b, c, d):
    """Make a-b and c-d slices of string s, inclusively"""

    list_slices = [s[a:b+1], s[c:d+1]]
    sliced_string = " ".join(list_slices)

    return sliced_string


# --------------------------------------------------
if __name__ == '__main__':
    main()
