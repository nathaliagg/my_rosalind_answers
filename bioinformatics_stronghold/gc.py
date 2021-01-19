#!/usr/bin/env python3

"""
Author : Nathalia Graf Grachet
Date   : 2021-01-15
Purpose: Bioinformatics Stronghold - Computing GC content
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
        description="""Computing GC content. Given at most 10 fast sequences
        of at most 1 kbp each, this program returns the sequence ID with the
        highest GC content, followed by the GC content of the sequence.""",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('input_file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        help='Input file, max 10 sequences of 1000 bp each')

    args = parser.parse_args()

    return args


# --------------------------------------------------
def main():
    """Compute GC"""

    args = get_args()

    sequences = make_seq_dict(args.input_file)

    # print(sequences)
    for i in find_highest_gc(sequences):
        print(i)


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
def test_len(dict_sequences):
    """Test len sequence < 1000"""

    for k, v in dict_sequences.items():
        if len(v['sequence']) > 1000:
            raise BadSequenceLength('Sequence must be shorter than 1000 nt.')


# --------------------------------------------------
def test_n_seqs(dict_sequences):
    """Test less than 10"""

    if len(dict_sequences.keys()) > 10:
        msg = 'Limit of 10 fasta sequences per file.'
        raise BadNumberSequences(msg)


# --------------------------------------------------
def make_seq_dict(file):
    """Parse input file into a dictionary"""

    seq_dict = {}

    for line in file.read().rstrip().split('\n'):
        if line.startswith('>'):
            header = line
            if header not in seq_dict:
                seq_dict[header] = {}
                seq_dict[header]['sequence'] = ''
                seq_dict[header]['gc'] = 0
        else:
            seq = line
            test_nucleotides(seq)
            seq_dict[header]['sequence'] += seq
            gc = calculate_gc(seq_dict[header]['sequence'])
            seq_dict[header]['gc'] = gc

    test_n_seqs(seq_dict)

    test_len(seq_dict)

    # print(seq_dict)

    return seq_dict


# --------------------------------------------------
def calculate_gc(string):
    """Compute GC content from a string"""

    string = string.upper()

    g = string.count('G')
    c = string.count('C')
    s = len(string)

    gc = (g+c)/s * 100

    gc = "{0:.6f}".format(gc)

    return gc


# --------------------------------------------------
def find_highest_gc(seq_dict):
    """Retrieve the sequence with highest GC content"""

    list_gc = []

    for k, v in seq_dict.items():
        p = (k[1:], v['gc'])
        list_gc.append(p)

    list_gc = sorted(list_gc, key=lambda x: x[1], reverse=True)

    # print(list_gc)

    return list_gc[0]


# --------------------------------------------------
if __name__ == '__main__':
    main()
