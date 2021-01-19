#!/usr/bin/env python3

"""tests for ini3.py"""


import os
import re
from subprocess import getstatusoutput


prg = '../ini3.py'
a_string = 'thisistheteststring,butamuchlongerstring.HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagainHumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.'
b_string = 'HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.'
a = 22
b = 27
c = 97
d = 102


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
    error_string = 'following arguments are required: str, int, int, int, int'
    assert re.findall(error_string, out, re.IGNORECASE)


# --------------------------------------------------
def test_len_str():
    """Output when the length of the string argument is greater than 200"""

    rv, out = getstatusoutput(f'{prg} {a_string} {a} {b} {c} {d}')
    assert rv != 0
    error_string = f"LengthString: Lenght of string {len(a_string)} must be less than 200"
    assert re.findall(error_string, out, re.IGNORECASE)


# --------------------------------------------------
def test_int_args():
    """Output when all arguments are correct"""

    rv, out = getstatusoutput(f'{prg} {b_string} {a} {b} {c} {d}')
    assert rv == 0
    assert out == 'Humpty Dumpty'


# --------------------------------------------------
