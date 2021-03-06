#!/usr/bin/env python3

"""tests for revc .py"""


import os
import re
from subprocess import getstatusoutput


prg = '../revc.py'
good_input = 'test_data/good_input_revc.txt'
bad_input = 'test_data/bad_input_revc.txt'
good_output = 'ACCGGGTTTT'

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

    rv, out = getstatusoutput(f'{prg} "{bad_input}"')
    assert rv != 0
    error_string = "Bad nucleotide sequence. Only ATCG allowed."
    assert re.findall(error_string, out, re.IGNORECASE)


# --------------------------------------------------
def test_good_output():
    """Test output with a good string"""

    rv, out = getstatusoutput(f'{prg} "{good_input}"')
    assert rv == 0
    assert out == good_output


# --------------------------------------------------
