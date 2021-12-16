#!/usr/bin/env python3
import sys


def solve(a: int, b: int, c: int):
    result = sum([7 - x for x in [a, b, c]])
    print(result)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    a = int(next(tokens))  # type: int
    b = int(next(tokens))  # type: int
    c = int(next(tokens))  # type: int
    solve(a, b, c)


if __name__ == "__main__":
    main()
