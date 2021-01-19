#!/usr/bin/env python3

"""
Author : Nathalia Graf Grachet
Date   : 2021-01-15
Purpose: Bioinformatics Stronghold - Complementing a Strand of DNA
"""

import argparse


class BadSequenceLength(Exception):
    """Base class for other exception """


class BadNucleotideSequence(Exception):
    """Base class for other exception """


# --------------------------------------------------
def get_args():
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description="""Complementing a Strand of DNA. Given a DNA string of
        at most 1000 bp, this program returns the reverse complement of the
        string.""",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('string',
                        metavar='str',
                        type=str,
                        help='A string of DNA nucleotides')

    args = parser.parse_args()

    return args


# --------------------------------------------------
def main():
    """Reverse complement"""

    args = get_args()
    # print(args)

    test_nucleotides(args.string)

    test_len_seq(args.string)

    print(rev_complement(args.string))


# --------------------------------------------------
def test_nucleotides(string):
    """Test there is anything other than A, T, C, G"""

    not_nt_list = []

    string = string.upper()

    for char in string:
        if char not in ['A', 'T', 'C', 'G']:
            not_nt_list.append(char)

    if len(not_nt_list) > 0:
        msg = "Bad nucleotide sequence. Only ATCG allowed."
        raise BadNucleotideSequence(msg)


# --------------------------------------------------
def test_len_seq(string):
    """Test len sequence < 1000"""

    if len(string) > 1000:
        raise BadSequenceLength('Sequence must be shorter than 1000 nt.')


# --------------------------------------------------
def rev_complement(string):
    """Make the reverse complement"""

    string = string.upper()

    string = string[::-1]

    to_replace = [('A', 't'), ('T', 'a'), ('C', 'g'), ('G', 'c')]

    for rc in to_replace:
        string = string.replace(rc[0], rc[1])

    string = string.upper()

    return string


# --------------------------------------------------
if __name__ == '__main__':
    main()
