#!/usr/bin/env python3

"""tests for ini2.py"""


import os
import re
from subprocess import getstatusoutput


prg = '../ini2.py'
a_string = 'a'
a = 3
b = 5
c = 2000


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
def test_str_args():
    """Output when a string argument is given"""

    rv, out = getstatusoutput(f'{prg} {a} {a_string}')
    assert rv != 0
    error_string = f"error: argument int: invalid int value: '{a_string}'"
    assert re.findall(error_string, out, re.IGNORECASE)


# --------------------------------------------------
def test_int_args():
    """Output when two integers is given"""

    h = (a*a) + (b*b)

    rv, out = getstatusoutput(f'{prg} {a} {b}')
    assert rv == 0
    assert out == str(h)


# --------------------------------------------------
def test_int_greater_than_1000():
    """Output when an integer is greater than 1000"""

    rv, out = getstatusoutput(f'{prg} {a} {c}')
    assert rv != 0
    error_string = f"error: argument int: invalid choice: {c}"
    assert re.findall(error_string, out, re.IGNORECASE)


# --------------------------------------------------
