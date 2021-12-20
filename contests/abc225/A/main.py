#!/usr/bin/env python3
import sys


def solve(S: str):
    x = len(set(list(S)))
    if x == 1:
        print(1)
    elif x == 2:
        print(3)
    else:
        print(6)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    solve(S)


if __name__ == "__main__":
    main()
