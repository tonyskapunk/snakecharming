# -*- coding: utf-8 -*-

import sys

# decorator?
def fibonacci(n):
    """ Returns n elements of the fibonacci series
    2 < n <= 2000000
    """
    fibo = [1, 2]
    if n >= 2000000:
        return fibo

    for i in range(2, n):
        fibo.append( sum(fibo[i-2:i]) )
    
    return fibo


def main():
    n = int(sys.argv[1])
    print(fibonacci(n))

if __name__ == "__main__":
    main()
