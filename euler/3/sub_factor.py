#!/usr/bin/python

import sys
import subprocess


def get_factors(n):
    """Gets all the prime factors of a number"""
    factors = []
    exit_code, output = subprocess.getstatusoutput(f"factor {n}")
    if exit_code == 0:
        _, fact_str = output.split(":")
        factors.extend(map(int, set(fact_str.strip().split())))

    return sorted(factors)


def main():
    try:
        n = int(sys.argv[1])
    except:
        print("Invalid number provided")
        sys.exit(1)

    f = get_factors(n)
    print(f)
    print(f[-1])


if __name__ == "__main__":
    main()
