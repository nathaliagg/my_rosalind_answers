#!/usr/bin/env python3

"""tests for fib.py"""


import os
import re
from subprocess import getstatusoutput


prg = '../fib.py'
good_n = 5
good_k = 3
good_output = '19'
bad_n = 50
bad_k = 10


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
    error_string = 'following arguments are required: int, int'
    assert re.findall(error_string, out, re.IGNORECASE)


# --------------------------------------------------
def test_bad_n():
    """Bad n argument"""

    rv, out = getstatusoutput(f'{prg} {bad_n} {good_k}')
    assert rv != 0
    error_string = "ValueError: n must be less than or equal to 40."
    assert re.findall(error_string, out, re.IGNORECASE)


# --------------------------------------------------
def test_bad_k():
    """Bad k argument"""

    rv, out = getstatusoutput(f'{prg} {good_n} {bad_k}')
    assert rv != 0
    error_string = "ValueError: k must be less than or equal to 5"
    assert re.findall(error_string, out, re.IGNORECASE)


# --------------------------------------------------
def test_good_args():
    """Output with good args"""

    rv, out = getstatusoutput(f'{prg} {good_n} {good_k}')
    assert rv == 0
    assert out == good_output


# --------------------------------------------------
