#!/usr/bin/env python3

"""
Author : Nathalia Graf Grachet
Date   : 2021-01-15
Purpose: Python Village - Working with Files
"""

import argparse


# define Python user-defined exceptions
class NumberLinesError(Exception):
    """Base class for other exceptions"""


# --------------------------------------------------
def get_args():
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description="""Working with Files. Given a file containing at most
        1000 lines, and assuming a 1-based numbering of line, this program
        returns a file containing all the even-numbered lines
        from the original file.""",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('input_file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        help='Input file, 1000 lines max')

    args = parser.parse_args()

    return args


# --------------------------------------------------
def main():
    """Does it all"""

    args = get_args()

    list_lines = args.input_file.read().rstrip().split("\n")

    test_n_lines(list_lines)

    even_lines = get_even_lines(list_lines)

    # with open('output_ini5.txt', 'w') as out:
    #     for line in even_lines:
    #         out.write(line+'\n')

    print("\n".join(even_lines))


# --------------------------------------------------
def test_n_lines(list_file):
    """Test if input file < 1000 lines"""

    if len(list_file) > 1000:
        msg = "Input file must have less than 1000 lines"
        raise NumberLinesError(msg)


# --------------------------------------------------
def get_even_lines(list_file):
    """Get all even lines == makes enumerate start at 1"""

    even_lines = []

    for index, line in enumerate(list_file, start=1):
        if index % 2 == 0:
            even_lines.append(line)

    return even_lines


# --------------------------------------------------
if __name__ == '__main__':
    main()
