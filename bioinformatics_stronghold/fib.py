#!/usr/bin/env python3

"""
Author : Nathalia Graf Grachet
Date   : 2021-01-15
Purpose: Bioinformatics Stronghold - Rabbits and Recurrence Relations
"""

import argparse


# --------------------------------------------------
def get_args():
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description="""Rabbits and Recurrence Relations. Given two positive
        integers, n <= 40 and k <= 5, this program returns the total number of
        rabbits pairs present after n months if we begin with 1 pair and in
        each generation, every pair of reproduction-age rabbist produces a
        litter of k rabbit pairs.""",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('int_n',
                        metavar='int',
                        type=int,
                        help='Integer n, n <= 40')

    parser.add_argument('int_k',
                        metavar='int',
                        type=int,
                        help='Integer k, k <= 5')

    args = parser.parse_args()

    return args


# --------------------------------------------------
def main():
    """Fibonacci's sequence"""

    args = get_args()
    # print(args)

    test_n(args.int_n)

    test_k(args.int_k)

    print(fibonacci(args.int_n, args.int_k))


# --------------------------------------------------
def test_n(n):
    """Assert n <= 40"""

    if n > 40:
        raise ValueError('n must be less than or equal to 40.')


# --------------------------------------------------
def test_k(k):
    """Assert k <= 5"""

    if k > 5:
        raise ValueError('k must be less than or equal to 5.')


# --------------------------------------------------
def fibonacci(n, k):
    """Fibs"""

    if n == 1:
        return 1

    elif n == 2:
        return 1

    else:
        return fibonacci(n-1, k) + k * fibonacci(n-2, k)


# --------------------------------------------------
if __name__ == '__main__':
    main()
