#!/usr/bin/env python3
import sys


def solve(x: int, y: int):
    if x == y:
        print(x)
    else:
        print(3 - (x + y))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    x = int(next(tokens))  # type: int
    y = int(next(tokens))  # type: int
    solve(x, y)


if __name__ == "__main__":
    main()
