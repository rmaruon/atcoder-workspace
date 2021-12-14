#!/usr/bin/env python3
import sys


def solve(a: int, b: int, c: int, d: int):
    print(max(a, b) - min(c, d))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    a = int(next(tokens))  # type: int
    b = int(next(tokens))  # type: int
    c = int(next(tokens))  # type: int
    d = int(next(tokens))  # type: int
    solve(a, b, c, d)


if __name__ == "__main__":
    main()
