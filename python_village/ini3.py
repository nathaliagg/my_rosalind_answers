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

    parser.add_argument('input_file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        help='Input file, string < 200, a, b, c, d integers')

    args = parser.parse_args()

    return args


# --------------------------------------------------
def main():
    """Slice string s, a through b, and
    c through d, inclusively."""

    args = get_args()
    # print(args)

    list_items = args.input_file.read().rstrip().split()

    string = list_items[0]

    test_length_string(string)

    integers = [int(x) for x in list_items[1:]]

    print(make_slices(string, integers))


# --------------------------------------------------
def test_length_string(s):
    """Test length of string, return error if > 200 letters"""

    if len(s) >= 200:
        raise LengthString(f"Length of string must be less than 200")


# --------------------------------------------------
def make_slices(s, list_ints):
    """Make a-b and c-d slices of string s, inclusively"""

    a, b, c, d = list_ints

    list_slices = [s[a:b+1], s[c:d+1]]
    sliced_string = " ".join(list_slices)

    return sliced_string


# --------------------------------------------------
if __name__ == '__main__':
    main()
