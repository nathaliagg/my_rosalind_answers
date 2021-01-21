#!/usr/bin/env python3

"""
Author : Nathalia Graf Grachet
Date   : 2021-01-15
Purpose: Bioinformatics Stronghold - Counting DNA Nucleotides
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
        description="""Counting DNA Nucleotides. Given a string of at
        most 1000 nucleotides, this program returns four integers separated
        by spaces, which reflect the count for A, C, G, and T nucleotides.""",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('input_file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        help='Input file, string < 1000 length')

    args = parser.parse_args()

    return args


# --------------------------------------------------
def main():
    """Count A, T, C, G"""

    args = get_args()
    # print(args)

    dna = args.input_file.read().rstrip().split()[0]

    test_nucleotides(dna)

    test_len_seq(dna)

    print(count_nt(dna))


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
def count_nt(string):
    """Count A, T, C, G"""

    string = string.upper()

    counts = []

    for nt in ['A', 'C', 'G', 'T']:
        counts.append(string.count(nt))

    s_counts = " ".join([str(x) for x in counts])

    return s_counts


# --------------------------------------------------
if __name__ == '__main__':
    main()
