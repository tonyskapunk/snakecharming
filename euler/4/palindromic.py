#!/usr/bin/python3

import sys


def palindromic(d):
    """Gets a palindromic number made from a product of two d-digit numbers"""
    # Get the upper limit of d digits, e.g 3 digits is 999
    a = 10 ** d - 1
    b = a
    # Get the lower limit of d digits, e.g. 3 digits is 100
    limit = 10 ** (d - 1)

    for x in range(a, limit - 1, -1):
        for y in range(b, limit - 1, -1):
            tmp = x * y
            if str(tmp) == str(tmp)[::-1]:
                print(x, y)
                return x * y

    return 0


def main():
    n = int(sys.argv[1])

    p = palindromic(n)
    print(p)


if __name__ == "__main__":
    main()
