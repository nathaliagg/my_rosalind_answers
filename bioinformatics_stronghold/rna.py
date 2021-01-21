#!/usr/bin/env python3

"""
Author : Nathalia Graf Grachet
Date   : 2021-01-15
Purpose: Bioinformatics Stronghold - Transcribing DNA into RNA
"""

import argparse


class BadNucleotideSequence(Exception):
    """Base class for other exception """


# --------------------------------------------------
def get_args():
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description="""Transcribing DNA into RNA. Given a DNA string, which
        corresponds to a coding strand, this program returns its transcribed
        RNA string.""",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('input_file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        help='Input file, string')

    args = parser.parse_args()

    return args


# --------------------------------------------------
def main():
    """Count A, T, C, G"""

    args = get_args()
    # print(args)

    rna = args.input_file.read().rstrip().split()[0]

    test_nucleotides(rna)

    print(transcribe_dna(rna))


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
def transcribe_dna(string):
    """Transcription, replace T with U"""

    string = string.upper()

    t_string = string.replace('T', 'U')

    return t_string


# --------------------------------------------------
if __name__ == '__main__':
    main()
