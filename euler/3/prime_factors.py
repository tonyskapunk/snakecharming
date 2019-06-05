#!/usr/bin/python3

import sys


def div_by(n, list_of_num):
    """Validates if a number is divisible by any number of a list"""
    for num in list_of_num:
        if not n % num:
            return True
    return False


def factors(n):
    """Obtain a list of prime factors of a number """
    _factors = []
    p = 1

    # Loop until half of n
    while p <= n // 2:
        p += 1
        if div_by(p, _factors):
            continue
        if not n % p:
            _factors.append(p)

    # Number given is a prime
    if not _factors:
        _factors.append(n)

    return _factors


def main():
    n = int(sys.argv[1])

    f = factors(n)
    print(f)
    print(f[-1])


if __name__ == "__main__":
    main()
