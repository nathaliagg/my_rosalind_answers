#!/usr/bin/env python3


"""tests for ini2.py"""


import os
import re
from subprocess import getstatusoutput


prg = '../ini2.py'
good_input = 'test_data/good_input_ini2.txt'
bad_input = 'test_data/bad_input_ini2.txt'
output = '34'


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
def test_1000():
    """Output with an int >= 1000"""

    rv, out = getstatusoutput(f'{prg} {bad_input}')
    assert rv != 0
    error_string = 'Integer must be less than 1000'
    assert re.findall(error_string, out, re.IGNORECASE)


# --------------------------------------------------
def test_good_input():
    """Test on good input"""

    rv, out = getstatusoutput(f'{prg} {good_input}')
    assert rv == 0
    assert out == output


# --------------------------------------------------
