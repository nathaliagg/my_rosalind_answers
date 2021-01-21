#!/usr/bin/env python3

"""tests for ini6.py"""

import os
import re
from subprocess import getstatusoutput

prg = '../ini6.py'
good_input = "test_data/good_input_ini6.txt"
bad_input = "test_data/bad_input_ini6.txt"

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
def test_bad_string():
    """Test output with bad string, >10000 characters"""

    rv, out = getstatusoutput(f'{prg} "{bad_input}"')
    assert rv != 0
    error_string = 'LengthStringError: Lenght of string must be less than 10000'
    assert re.findall(error_string, out, re.IGNORECASE)


# --------------------------------------------------
def test_good_string():
    """Output when no args are provided"""

    rv, out = getstatusoutput(f'{prg} "{good_input}"')
    # assert "\n" in out
    assert out.count("\n") > 2


# --------------------------------------------------
