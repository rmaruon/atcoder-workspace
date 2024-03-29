#!/usr/bin/env python3
import sys


def solve(N: int):
    if 1 <= N <= 125:
        print(4)
    elif 126 <= N <= 211:
        print(6)
    else:
        print(8)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    solve(N)


if __name__ == "__main__":
    main()
