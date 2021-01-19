#!/usr/bin/env python3

"""
Author : Nathalia Graf Grachet
Date   : 2021-01-18
Purpose: Bioinformatics Stronghold - Counting Point Mutations
"""


import argparse


class BadSequenceLength(Exception):
    """Base class for other exception """


class BadNucleotideSequence(Exception):
    """Base class for other exception """


class BadNumberSequences(Exception):
    """Base class for other exception """


# --------------------------------------------------
def get_args():
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description="""Counting Point Mutations. Given a file with
        two DNA strings, s and t of equal length and not larger than 1000 bp,
        this program returns the Hamming distance. The Hamming distance
        corresponds to the number of mismatched nucleotides.""",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('input_file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        help='Input file, max 2 sequences of 1000 bp each')

    args = parser.parse_args()

    return args


# --------------------------------------------------
def main():
    """Hamming distance"""

    args = get_args()

    list_seqs = args.input_file.read().rstrip().split()

    test_n_seqs(list_seqs)

    for seq in list_seqs:
        test_nucleotides(seq)
        test_len(seq)

    print(hamming(list_seqs))


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
def test_len(string):
    """Test len sequence < 1000"""

    if len(string) > 1000:
        raise BadSequenceLength('Sequence must be shorter than 1000 nt.')


# --------------------------------------------------
def test_n_seqs(list_sequences):
    """Test less than 10"""

    if len(list_sequences) > 2:
        msg = 'Limit of 2 nucleotide sequence per file.'
        raise BadNumberSequences(msg)


# --------------------------------------------------
def hamming(list_sequences):
    """Compute Hamming distance of two DNA strings"""

    string_a, string_b = list_sequences

    hamm = 0

    for nt_a, nt_b in list(zip(string_a, string_b)):
        if nt_a != nt_b:
            hamm += 1

    return hamm


# --------------------------------------------------
if __name__ == '__main__':
    main()
