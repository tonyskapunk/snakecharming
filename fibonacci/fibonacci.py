#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys


def fibonacci(n):
    """ Returns n elements of the fibonacci series"""
    fibo = [1, 1]
    if n < 1 or n > 2_000_000:
        return []
    elif n < 2:
        return fibo[:n]

    for i in range(2, n):
        fibo.append(sum(fibo[i - 2 : i]))

    return fibo


def even_fibonacci(n):
    """Return the sum of even elements of the fibonacci series"""
    fibo = [1, 1]
    even = 0
    if n < 2 or n > 2_000_000:
        return 0

    while n > 2:
        n -= 1
        f = sum(fibo)
        if f % 2 == 0:
            even += f
        fibo = [fibo[-1], f]

    return even


def main():
    name = os.path.basename(__file__).split(".")[0]
    if len(sys.argv) != 2:
        print(f"Error: {name} takes exactly 1 argument")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except:
        print(f"Error: Argument has to be an int between 2 and 2000000")
        sys.exit(1)

    # Print result to a file using "name_n"
    with open(f"{name}_{n}", "w") as f:
        f.write(str(even_fibonacci(n)))


if __name__ == "__main__":
    main()
