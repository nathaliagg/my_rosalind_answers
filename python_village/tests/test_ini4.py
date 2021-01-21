#!/usr/bin/env python3

"""tests for ini4.py"""

import os
import re
from subprocess import getstatusoutput

prg = '../ini4.py'
good_input = "test_data/good_input_ini4.txt"
bad_input1 = "test_data/bad_input1_ini4.txt"
bad_input2 = "test_data/bad_input2_ini4.txt"

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
def test_b():
    """Test if b < 10000"""

    rv, out = getstatusoutput(f'{prg} {bad_input2}')
    assert rv != 0
    error_string = f"IntegerValueError:  b must be less than 10000"
    assert re.findall(error_string, out, re.IGNORECASE)


# --------------------------------------------------
def test_a():
    """Test if a < b"""

    rv, out = getstatusoutput(f'{prg} {bad_input1}')
    assert rv != 0
    error_string = f"IntegerValueError: a must be less than b"
    assert re.findall(error_string, out, re.IGNORECASE)


# --------------------------------------------------
def test_correct_output():
    """Test correct output"""

    rv, out = getstatusoutput(f'{prg} {good_input}')
    assert rv == 0
    assert out == str(7500)


# --------------------------------------------------
