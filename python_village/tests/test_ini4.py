#!/usr/bin/env python3

"""tests for ini4.py"""

import os
import re
from subprocess import getstatusoutput

prg = '../ini4.py'
a_right = 100
b_right = 200
a_wrong = 300
b_wrong = 20000

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
def test_b():
    """Test if b < 10000"""

    rv, out = getstatusoutput(f'{prg} {a_right} {b_wrong}')
    assert rv != 0
    error_string = f"IntegerValueError:  b, {b_wrong}, must be less than 10000"
    assert re.findall(error_string, out, re.IGNORECASE)


# --------------------------------------------------
def test_a():
    """Test if a < b"""

    rv, out = getstatusoutput(f'{prg} {a_wrong} {b_right}')
    assert rv != 0
    error_string = f"IntegerValueError: a, {a_wrong}, must be less than {b_right}"
    assert re.findall(error_string, out, re.IGNORECASE)


# --------------------------------------------------
def test_correct_output():
    """Test correct output"""

    rv, out = getstatusoutput(f'{prg} {a_right} {b_right}')
    assert rv == 0
    assert out == str(7500)


# --------------------------------------------------
