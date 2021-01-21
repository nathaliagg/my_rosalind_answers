#!/usr/bin/env python3

"""tests for ini3.py"""


import os
import re
from subprocess import getstatusoutput


prg = '../ini3.py'
bad_input = 'test_data/bad_input_ini3.txt'
good_input = 'test_data/good_input_ini3.txt'


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
def test_len_str():
    """Output when the length of the string argument is greater than 200"""

    rv, out = getstatusoutput(f'{prg} {bad_input}')
    assert rv != 0
    error_string = f"LengthString: Length of string must be less than 200"
    assert re.findall(error_string, out, re.IGNORECASE)


# --------------------------------------------------
def test_int_args():
    """Output when all arguments are correct"""

    rv, out = getstatusoutput(f'{prg} {good_input}')
    assert rv == 0
    assert out == 'Humpty Dumpty'


# --------------------------------------------------
