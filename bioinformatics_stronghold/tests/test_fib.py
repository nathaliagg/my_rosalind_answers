#!/usr/bin/env python3

"""tests for fib.py"""


import os
import re
from subprocess import getstatusoutput


prg = '../fib.py'
good_input = 'test_data/good_input_fib.txt'
good_output = '19'
bad_input1 = 'test_data/bad_input1_fib.txt'
bad_input2 = 'test_data/bad_input2_fib.txt'


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
def test_bad_n():
    """Bad n argument"""

    rv, out = getstatusoutput(f'{prg} {bad_input1}')
    assert rv != 0
    error_string = "ValueError: n must be less than or equal to 40."
    assert re.findall(error_string, out, re.IGNORECASE)


# --------------------------------------------------
def test_bad_k():
    """Bad k argument"""

    rv, out = getstatusoutput(f'{prg} {bad_input2}')
    assert rv != 0
    error_string = "ValueError: k must be less than or equal to 5"
    assert re.findall(error_string, out, re.IGNORECASE)


# --------------------------------------------------
def test_good_args():
    """Output with good args"""

    rv, out = getstatusoutput(f'{prg} {good_input}')
    assert rv == 0
    assert out == good_output


# --------------------------------------------------
