#!/usr/bin/env python3

"""tests for hamm.py"""


import os
import re
from subprocess import getstatusoutput


prg = '../hamm.py'
bad_file1 = "test_data/bad_input_hamm_1.txt"
bad_file2 = "test_data/bad_input_hamm_2.txt"
good_file = "test_data/good_input_hamm.txt"
good_output = '7'

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
def test_bad_file1():
    """Test with a file with more than 10 seqs"""

    rv, out = getstatusoutput(f'{prg} {bad_file1}')
    assert rv != 0
    error_string = "Limit of 2 nucleotide sequence per file"
    assert re.findall(error_string, out, re.IGNORECASE)


# --------------------------------------------------
def test_bad_file2():
    """Test with long sequence"""

    rv, out = getstatusoutput(f'{prg} {bad_file2}')
    assert rv != 0
    error_string = "BadSequenceLength: Sequence must be shorter than 1000 nt."
    assert re.findall(error_string, out, re.IGNORECASE)


# --------------------------------------------------
def test_good_args():
    """Test with a good input file"""

    rv, out = getstatusoutput(f'{prg} {good_file}')
    assert rv == 0
    assert out == good_output


# --------------------------------------------------
