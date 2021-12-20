#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(X: int):
    if X >= 100 and X % 100 == 0:
        print(YES)
    else:
        print(NO)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    X = int(next(tokens))  # type: int
    solve(X)


if __name__ == "__main__":
    main()
