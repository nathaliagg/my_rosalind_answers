#!/usr/bin/env python3

"""tests for ini5.py"""

import os
import re
from subprocess import getstatusoutput

prg = '../ini5.py'
wrong_file = "a_file_name.txt"
bad_input = "bad_input_ini5.txt"
good_input = "good_input_ini5.txt"
good_output = "good_output_ini5.txt"
output_program = "output_ini5.txt"


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
def test_file_doesnt_exist():
    """Output when file does not exist"""

    rv, out = getstatusoutput(f'{prg} {wrong_file}')
    assert rv != 0
    error_string = f"No such file or directory: '{wrong_file}'"
    assert re.findall(error_string, out, re.IGNORECASE)


# --------------------------------------------------
def test_bad_input_file():
    """Output when file has more than 1000 lines"""

    rv, out = getstatusoutput(f'{prg} {bad_input}')
    assert rv != 0
    error_string = f"NumberLinesError: Input file must have less than 1000 lines"
    assert re.findall(error_string, out, re.IGNORECASE)


# --------------------------------------------------
def test_good_input_file():
    """Output when file is good"""

    rv, out = getstatusoutput(f'{prg} {good_input}')
    assert rv == 0
    assert out == ""
    assert os.path.exists(output_program)


# --------------------------------------------------
def test_got_even_lines():
    """Test if program got even lines"""

    output_test = open(good_output).read().rstrip().split("\n")
    good_out_list = open(output_program).read().rstrip().split("\n")

    assert output_test == good_out_list


# --------------------------------------------------
