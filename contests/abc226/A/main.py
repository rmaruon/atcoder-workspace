#!/usr/bin/env python3
import sys


def solve(X: float):
    result = int(round(X + 0.0001, 0))
    print(result)


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
