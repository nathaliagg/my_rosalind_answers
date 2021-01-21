#!/usr/bin/env python3

"""tests for dna.py"""


import os
import re
from subprocess import getstatusoutput


prg = '../dna.py'
good_input = 'test_data/good_input_dna.txt'
bad_input1 = 'test_data/bad_input1_dna.txt'
bad_input2 = 'test_data/bad_input2_dna.txt'
good_output = '20 12 17 21'

# --------------------------------------------------
def test_exists():
    """Exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """Usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_no_args():
    """Output when no args are provided"""

    rv, out = getstatusoutput(f'{prg}')
    assert rv != 0
    error_string = 'following arguments are required: FILE'
    assert re.findall(error_string, out, re.IGNORECASE)


# --------------------------------------------------
def test_bad_args():
    """Test with a bad string == other than A, T, C, G"""

    rv, out = getstatusoutput(f'{prg} "{bad_input1}"')
    assert rv != 0
    error_string = "Bad nucleotide sequence. Only ATCG allowed."
    assert re.findall(error_string, out, re.IGNORECASE)


# --------------------------------------------------
def test_long_seq():
    """Test with long sequence"""

    rv, out = getstatusoutput(f'{prg} "{bad_input2}"')
    assert rv != 0
    error_string = "BadSequenceLength: Sequence must be shorter than 1000 nt."
    assert re.findall(error_string, out, re.IGNORECASE)


# --------------------------------------------------
def test_good_output():
    """Test output with a good string"""

    rv, out = getstatusoutput(f'{prg} "{good_input}"')
    assert rv == 0
    assert out == good_output
    assert len(out.split()) == 4


# --------------------------------------------------
