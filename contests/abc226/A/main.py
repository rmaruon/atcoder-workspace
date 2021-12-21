#!/usr/bin/env python3
import sys


def solve(X: float):
    a, b = str(X).split(".")

    if int(b[0]) >= 5:
        print(int(a) + 1)
    else:
        print(a)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    X = float(next(tokens))  # type: float
    solve(X)


if __name__ == "__main__":
    main()
