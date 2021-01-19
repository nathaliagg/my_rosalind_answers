#!/usr/bin/env python3

"""
Author : Nathalia Graf Grachet
Date   : 2021-01-15
Purpose: Python Village - Dictionaries
"""

import argparse


# define Python user-defined exceptions
class LengthStringError(Exception):
    """Base class for other exceptions"""


# --------------------------------------------------
def get_args():
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description="""Dictionaries. Given a string of maximum 10000 characters,
        this program returns the number of occurences of each word. Words are
        case-sensitive, separated by spaces, and the lines in the output can
        be in any order.""",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('string',
                        metavar='str',
                        type=str,
                        help='A string, 10000 letters max.')

    args = parser.parse_args()

    return args


# --------------------------------------------------
def main():
    """Does it all"""

    args = get_args()

    test_length_string(args.string)

    for k,v in get_word_count(args.string).items():
        print(k,v)


# --------------------------------------------------
def test_length_string(s):
    """Test length of string, return error if > 10000 characters"""

    if len(s) >= 10000:
        raise LengthStringError("Lenght of string must be less than 10000")


# --------------------------------------------------
def get_word_count(s):
    """Get word count in string s"""

    word_count = {}

    for word in s.split(' '):
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1

    return word_count


# --------------------------------------------------
if __name__ == '__main__':
    main()
